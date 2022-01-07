class Memory:

    def __init__(self):
        self.symbols = {}

    def has_key(self, name):  # variable name
        return name in self.symbols

    def get(self, name):  # gets from memory current value of variable <name>
        if name in self.symbols:
            return self.symbols[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.symbols[name] = value


class MemoryStack:

    def __init__(self):  # initialize memory stack with memory <memory>
        self.stack = [Memory()]

    def get(self, name):  # gets from memory stack current value of variable <name>
        for i in range(len(self.stack)-1, -1, -1) :
            memory = self.stack[i]
            if name in memory.symbols:
                return memory.get(name)
        return None

    def insert(self, name, value):  # inserts into memory stack variable <name> with value <value>
        self.stack[-1].put(name, value)

    def set(self, name, value):  # sets variable <name> to value <value>
        for i in range(len(self.stack)-1, -1, -1):
            memory = self.stack[i]
            if name in memory.symbols:
                memory.symbols[name] = value
                return

    # def push(self):  # pushes memory <memory> onto the stack
    #     self.stack.append(Memory())
    #
    # def pop(self):  # pops the top memory from the stack
    #     self.stack.pop()
