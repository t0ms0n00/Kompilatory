class Memory:

    def __init__(self, name):
        self.name = name
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
        self.stack = [Memory('global')]

    def get(self, name):  # gets from memory stack current value of variable <name>
        for i in range(len(self.stack)-1, -1, -1) :
            memory = self.stack[i]
            if name in memory.symbols:
                return memory.get(name)
        return None

    def insert(self, name, value):  # inserts into memory stack variable <name> with value <value>
        for i in range(len(self.stack) - 1, -1, -1):
            memory = self.stack[i]
            if memory.name in ["global", "block"]:
                self.stack[i].put(name, value)
                break

    def set(self, name, value):  # sets variable <name> to value <value>
        for i in range(len(self.stack) - 1, -1, -1):
            memory = self.stack[i]
            if memory.name in ["global", "block"] and name in memory.symbols:
                self.stack[i].put(name, value)
                break

    def push(self, name):  # pushes memory <memory> onto the stack
        self.stack.append(Memory(name))

    def pop(self):  # pops the top memory from the stack
        self.stack.pop()

    def get_last_memory_name(self):
        return self.stack[-1].name
