import AST
from SymbolTable import *
from OperationTypes import ttype


class NodeVisitor(object):
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.actual_scope = SymbolTable(None, 'main')
        self.loop_depth = 0 # licznik zagnieżdżonych pętli, aby continue/ break na pewno były w pętli
        self.error = False

    def visit_Program(self, node):
        if node.instructions is not None:
            self.visit(node.instructions)

    def visit_Instructions(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_Instruction(self, node):
        self.visit(node.instruction)

    def visit_Block(self, node):
        self.actual_scope = self.actual_scope.pushScope("block")
        self.visit(node.instructions)
        self.actual_scope = self.actual_scope.popScope()

    def visit_If(self, node):
        self.actual_scope = self.actual_scope.pushScope('if')
        self.visit(node.condition)
        self.visit(node.then_instr)
        self.actual_scope = self.actual_scope.popScope()
        if node.else_instr is not None:
            self.actual_scope = self.actual_scope.pushScope('else')
            self.visit(node.else_instr)
            self.actual_scope = self.actual_scope.popScope()

    def visit_For(self, node):
        self.actual_scope = self.actual_scope.pushScope('for')
        self.loop_depth += 1
        result_type = self.visit(node.range) # visit_Range
        if result_type != 'unknown':
            symbol = VariableSymbol(node.variable, result_type)
            self.actual_scope.put(node.variable, symbol)
        self.visit(node.instruction)
        self.loop_depth -= 1
        self.actual_scope = self.actual_scope.popScope()

    def visit_Range(self, node):
        left = self.visit(node.from_value)
        right = self.visit(node.to_value)
        if left != 'int' or right != 'int': # jeśli nie przyjmuje dwóch intów to źle
            print("Line {}: Incompatible range types {} and {} for instruction for".format(node.lineno, left, right))
            self.error = True
            return 'unknown'
        return 'int'

    def visit_While(self, node):
        self.actual_scope = self.actual_scope.pushScope('while')
        self.loop_depth += 1
        self.visit(node.condition)
        self.visit(node.instruction)
        self.loop_depth -= 1
        self.actual_scope = self.actual_scope.popScope()

    def visit_Break(self, node):
        if self.loop_depth == 0:
            print("Line {}: Break outside the loop".format(node.lineno))
            self.error = True

    def visit_Continue(self, node):
        if self.loop_depth == 0:
            print("Line {}: Continue outside the loop".format(node.lineno))
            self.error = True

    def visit_Return(self, node):
        if node.value is not None:
            result_type = self.visit(node.value)
            if result_type == 'unknown': # jeśli typ jest nieznany to znaczy że jest źle (bo niżej gdzieś było źle)
                print("Line {}: Cannot return unknown type".format(node.lineno))
                self.error = True

    def visit_Print(self, node):
        for expression in node.expressions.expressions:
            result_type = self.visit(expression)
            if result_type == 'unknown': # podobnie jak return
                print("Line {}: Cannot print unknown type".format(node.lineno))
                self.error = True

    def visit_Expr(self, node):
        return self.visit(node.expression)

    def visit_Expressions(self, node):
        for expression in node.expressions:
            self.visit(expression)

    def visit_Singleton(self, node):
        if type(node.singleton) == str: # jeśli znajdziemy typ podstawowy to ok, inaczej zwracamy że nieznany
            return 'str'
        elif type(node.singleton) == int:
            return 'int'
        elif type(node.singleton) == float:
            return 'float'
        return 'unknown'

    def visit_Vector(self, node):
        expressions = node.expressions.expressions if node.expressions is not None else [] # wyciągamy elementy wektora
        types_inside_vector = set() # szukamy różnych typów zawartych w strukturze danych
        for expr in expressions:
            result_type = self.visit(expr)
            result_type = 'float' if result_type == 'int' else result_type # założenie że inty i floaty można trzymać
            # razem (bo reguły operacji pozwalają na operacje binarne int z float), zatem castujemy element typu int na float
            result_type = 'matrix' if isinstance(result_type, VariableSymbol) and result_type.dim2 is not None else result_type
            # jeśli visit_Variable zwróciło info o macierzy lub wektorze to dajemy ładniejszy alias nazwy typu
            result_type = 'vector' if isinstance(result_type, VariableSymbol) and result_type.dim2 is None else result_type
            types_inside_vector.add(result_type)
        flag = False
        if len(types_inside_vector) > 1: # wymaganie że elementy jednakowego typu wewnątrz
            if 'vector' in types_inside_vector:
                print("Line {}: Matrix should contain one type, but contains {}".format(node.lineno, types_inside_vector))
                self.error = True
            else:
                print("Line {}: Vector should contain one type, but contains {}".format(node.lineno, types_inside_vector))
                self.error = True
            flag = True
        if 'matrix' in types_inside_vector: # pilnuje żeby nie było macierzy więcej niż 2-d
            print("Line {}: Matrix must be 2 dimensional".format(node.lineno))
            self.error = True
            flag = True
        if 'str' in types_inside_vector: # nie chcemy trzymać stringów w macierzach
            if 'vector' in types_inside_vector:
                print("Line {}: Matrix cannot have str type inside".format(node.lineno))
                self.error = True
            else:
                print("Line {}: Vector cannot have str type inside".format(node.lineno))
                self.error = True
            flag = True
        if 'unknown' in types_inside_vector: # jeśli jakiś typ był nieznany w strukturze dodajemy też taki komunikat wskazujący że gdzieś jest błąd
            if 'vector' in types_inside_vector:
                print("Line {}: Matrix cannot have unknown type inside".format(node.lineno))
                self.error = True
            else:
                print("Line {}: Vector cannot have unknown type inside".format(node.lineno))
                self.error = True
            flag = True
        if flag: # jeśli cokolwiek było źle, to typ jest nieznany, bo może np zawierać dwa różne typy w sobie, lub być macierzą o ponad 2 wymiarach
            return 'unknown'
        if 'vector' in types_inside_vector: # fragment sprawdzający czy wektory w macierzy są jednakowych rozmiarów, zwraca błąd, gdy znajdzie 2 różne długości
            vector_len = set()
            rows = 0
            for expression in node.expressions.expressions:
                if expression.expression.expressions is None:
                    return VariableSymbol(None, 'float', 0, None)
                rows += 1
                vector_len.add(len(expression.expression.expressions.expressions))
                if len(vector_len) > 1:
                    print("Line {}: Matrix should have vectors equal sizes, but has {}".format(node.lineno, vector_len))
                    self.error = True
                    return 'unknown'
            cols = vector_len.pop()
            return VariableSymbol(None, 'float', rows, cols) # zwracamy typ macierz, bo przeszła wszystkie swoje warunki
        return VariableSymbol(None, 'float', len(expressions))# zwracamy typ wektor, bo przeszedł wszystkie swoje warunki

    def visit_Assign(self, node):
        if node.operator == "=":
            left = node.variable
            if left.index2 is not None:
                matrix = self.actual_scope.get(left.name)
                if left.index1 > matrix.dim1 or left.index2 > matrix.dim2:
                    print("Line {}: Index out of matrix range".format(node.lineno))
                    self.error = True
            elif left.index1 is not None:
                vector = self.actual_scope.get(left.name)
                if left.index1 > vector.dim1:
                    print("Line {}: Index out of vector range".format(node.lineno))
                    self.error = True
            right = self.visit(node.expression)
            if right == 'unknown': # nie możemy przypisać typu którego nie znamy
                print("Line {}: Cannot assign unknown type to variable".format(node.lineno))
                self.error = True
            elif right == 'str' or right == 'int' or right == 'float': # dodanie do tablicy symboli z typem prymitywnym
                symbol = VariableSymbol(node.variable.name, right)
                if left.index1 is None:
                    self.actual_scope.put(node.variable.name, symbol)
            else: # dodanie do tablicy symboli obiektu wektora lub macierzy
                symbol = VariableSymbol(node.variable.name, right.type, right.dim1, right.dim2)
                if left.index1 is None:
                    self.actual_scope.put(node.variable.name, symbol)

        else: # calc_assign
            operator = self.visit(node.operator)
            if self.visit(node.variable) is None: # zmienna po lewej stronie musi istnieć a += b <=> a = a + b
                print("Line {}: Variable {} not defined".format(node.lineno, node.variable.name))
                self.error = True
                return 'unknown'
            left = self.visit(node.variable)
            right = self.visit(node.expression)
            if right == 'unknown': # typ przypisywany musi być znany
                print("Line {}: Cannot assign unknown type to variable".format(node.lineno))
                self.error = True
            elif ttype[operator][left][right] == 'unknown': # operacja musi być możliwa do wykonania
                print("Line {}: Incompatible assign operation types {} and {} for operator {}".format(node.lineno, left, right, operator))
                self.error = True

    def visit_CalcAssign(self, node):
        return node.operator

    def visit_Variable(self, node):
        if node.name not in self.actual_scope.symbols.keys(): # odwołanie do nieistniejącej zmiennej
            print("Line {}: Reference to not defined object {}".format(node.lineno, node.name))
            self.error = True
            return 'unknown'
        ref_to = self.actual_scope.symbols[node.name]
        dim1 = self.actual_scope.symbols[node.name].dim1
        dim2 = self.actual_scope.symbols[node.name].dim2
        if node.index1 is not None and dim1 is None: # 4 kolejne: sprawdzanie odwołań do indeksów tablic
            print("Line {}: Reference to the dimension that not exists".format(node.lineno))
            self.error = True
            return 'unknown'
        if node.index2 is not None and dim2 is None:
            print("Line {}: Reference to the dimension that not exists".format(node.lineno))
            self.error = True
            return 'unknown'
        if node.index2 is not None and node.index1 is not None: # matrix
            if node.index1 >= dim1 or node.index2 >= dim2:
                print("Line {}: Index out of matrix range".format(node.lineno))
                self.error = True
                return 'unknown'
        if node.index1 is not None and node.index1 >= dim1: # vector
            print("Line {}: Index out of vector range".format(node.lineno))
            self.error = True
            return 'unknown'
        if node.index1 is not None and node.index2 is not None: #referencja z dwoma indeksami w macierzy
            return ref_to.type
        if node.index1 is not None:
            if dim2 is None: # odwołanie do elementu
                return ref_to.type
            else: # referencja do całego wektora
                return VariableSymbol(None, 'float', dim2)
        if self.actual_scope.symbols[node.name].dim2 is not None: #macierz
            return VariableSymbol(node.name, 'float', dim1, dim2)
        elif self.actual_scope.symbols[node.name].dim1 is not None: # wektor
            return VariableSymbol(node.name, 'float', dim1)
        else: # typ prymitywny
            singleton_type = self.actual_scope.symbols[node.name].type
            return singleton_type

    def visit_Comparator(self, node):
        return node.comparator

    def visit_Condition(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        comparator = self.visit(node.comparator)
        result_type = ttype[comparator][left][right]
        if result_type == 'unknown':
            print('Line {}: Incompatible types {} and {} for operation {}'.format(node.lineno, left, right, comparator))
            self.error = True

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        operator = node.operator

        result_type = ttype[operator][left][right]
        if result_type == 'unknown': # zwróć typ nieznany gdy operacja nie może być wykonana
            print('Line {}: Incompatible types {} and {} for operation {}'.format(node.lineno, left, right, operator))
            self.error = True

        # wpp zwróć typ wynikowy operacji
        return result_type

    def visit_MatrixOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        operator = node.operator
        left_type = 'matrix' if isinstance(left, VariableSymbol) and left.dim2 is not None else left # nadawanie aliasów typom macierz i wektor
        left_type = 'vector' if isinstance(left, VariableSymbol) and left.dim2 is None else left_type
        right_type = 'matrix' if isinstance(right, VariableSymbol) and right.dim2 is not None else right
        right_type = 'vector' if isinstance(right, VariableSymbol) and right.dim2 is None else right_type
        if ttype[operator][left_type][right_type] == 'unknown': # operacja niemożliwa do wykonania na danych typach
            print('Line {}: Incompatible types {} and {} for operation {}'.format(node.lineno, left_type, right_type, operator))
            self.error = True
            return 'unknown'
        elif left.dim1 != right.dim1 or left.dim2 != right.dim2: # niezgodność wymiarów
            print('Line {}: {} objects should have equal dimensions, but has: {} and {}'.
                  format(node.lineno, left_type, (left.dim1, left.dim2), (right.dim1, right.dim2)))
            self.error = True
            return 'unknown'
        return VariableSymbol(None, 'float', left.dim1, left.dim2)

    def visit_UMinus(self, node):
        expr_type = self.visit(node.expression)
        expr_type = 'matrix' if isinstance(expr_type,
                                             VariableSymbol) and expr_type.dim2 is not None else expr_type
        expr_type = 'vector' if isinstance(expr_type, VariableSymbol) and expr_type.dim2 is None else expr_type

        if ttype['unary'][expr_type][None] == 'unknown':
            print("Line {}: Unary minus cannot be before type {}".format(node.lineno, expr_type))
            self.error = True
            return 'unknown'
        return ttype['unary'][expr_type][None]

    def visit_Transpose(self, node):
        result_type = self.visit(node.expression)
        result_type = 'matrix' if isinstance(result_type,
                                             VariableSymbol) and result_type.dim2 is not None else result_type
        result_type = 'vector' if isinstance(result_type, VariableSymbol) and result_type.dim2 is None else result_type
        if ttype['transpose'][result_type][None] == 'unknown':
            print("Line {}: Cannot transpose {} type".format(node.lineno, result_type))
            self.error = True
            return 'unknown'
        return result_type

    def visit_MatrixFunc(self, node):
        func = self.visit(node.func)
        dim1 = node.dim1
        dim2 = node.dim2
        flag = False
        if func == 'eye':
            if dim2 is not None: # funkcja eye musi przyjąć 1 parametr bo wystarczy bo macierz musi być kwadratowa
                print("Line {}: Too many arguments for function eye".format(node.lineno))
                self.error = True
                flag = True
            if dim1 <= 0: # niepoprawny rozmiar macierzy
                print("Line {}: Dimension for function eye should be positive, but got {}".format(node.lineno, dim1))
                self.error = True
                flag = True
            if type(dim1) != int: # niepoprawny typ rozmiaru macierzy
                print("Line {}: Function eye takes int parameter, but got type {}".format(node.lineno, type(dim1)))
                self.error = True
                flag = True
            if flag == False: # jeśli wszystko było ok to zwracamy strukturę danych
                return VariableSymbol(None, 'int', dim1, dim1)
        else: # funkcje zeros i ones - mogą przyjmować 2 parametry - macierz prostokątna
            if dim2 is None: # vector
                if dim1 <= 0:
                    print("Line {}: Dimension for function {} should be positive, but got {}".format(node.lineno, node.func, dim1))
                    self.error = True
                    flag = True
                if type(dim1) != int:
                    print("Line {}: Function {} takes int parameter, but got type {}".format(node.lineno, node.func, type(dim1)))
                    self.error = True
                    flag = True
                if flag == False:
                    return VariableSymbol(None, 'int', dim1)
            else: #matrix
                if dim1 <= 0 or dim2 <= 0:
                    print("Line {}: Dimension for function {} should be positive, but got {}".format(node.lineno, node.func, dim1))
                    self.error = True
                    flag = True
                if type(dim1) != int or type(dim2) != int:
                    print("Line {}: Function {} takes int parameter, but got type {}".format(node.lineno, node.func, type(dim1)))
                    self.error = True
                    flag = True
                if flag == False:
                    return VariableSymbol(None, 'int', dim1, dim2)
        return 'unknown'

    def visit_Function(self, node):
        return node.func
