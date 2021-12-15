import copy


class Symbol:
    pass


class VariableSymbol(Symbol):

    def __init__(self, name, type, dim1=None, dim2=None):
        self.name = name
        self.type = type
        self.dim1 = dim1
        self.dim2 = dim2

    def __repr__(self): # ładniejszy print typu wektor i macierz, uwzględnia ich wymiary
        if self.dim1 is None:
            return self.type
        if self.dim2 is None:
            return 'Vector[{}]'.format(self.dim1)
        return 'Matrix[{}][{}]'.format(self.dim1, self.dim2)


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.symbols = {}
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        return self.symbols[name]
    #

    def getParentScope(self):
        return self.parent
    #

    def pushScope(self, name):
        newScope = SymbolTable(self, name)
        newScope.parent = self
        newScope.symbols = copy.deepcopy(self.symbols) # do wyższego zakresu dodajemy wszystkie zmienne zadeklarowane w rodzicu
        return newScope
    #

    def popScope(self):
        return self.parent if self.parent is not None else print("Popping main scope is not allowed")
        # dodaliśmy kontrolę aby nigdzie nie wystąpił błąd przy użyciu funkcji pop
