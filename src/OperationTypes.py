from collections import defaultdict

ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 'unknown')))

ttype['+']['int']['int'] = 'int'
ttype['+']['float']['float'] = 'float'
ttype['+']['int']['float'] = 'float'
ttype['+']['float']['int'] = 'float'
ttype['+']['string']['string'] = 'string'

ttype['-']['int']['int'] = 'int'
ttype['-']['float']['float'] = 'float'
ttype['-']['int']['float'] = 'float'
ttype['-']['float']['int'] = 'float'

ttype['*']['int']['int'] = 'int'
ttype['*']['float']['float'] = 'float'
ttype['*']['int']['float'] = 'float'
ttype['*']['float']['int'] = 'float'

ttype['/']['int']['int'] = 'float'
ttype['/']['float']['float'] = 'float'
ttype['/']['int']['float'] = 'float'
ttype['/']['float']['int'] = 'float'

ttype['+=']['int']['int'] = 'int'
ttype['+=']['float']['float'] = 'float'
ttype['+=']['int']['float'] = 'float'
ttype['+=']['float']['int'] = 'float'

ttype['-=']['int']['int'] = 'int'
ttype['-=']['float']['float'] = 'float'
ttype['-=']['int']['float'] = 'float'
ttype['-=']['float']['int'] = 'float'

ttype['*=']['int']['int'] = 'int'
ttype['*=']['float']['float'] = 'float'
ttype['*=']['int']['float'] = 'float'
ttype['*=']['float']['int'] = 'float'

ttype['/=']['int']['int'] = 'int'
ttype['/=']['float']['float'] = 'float'
ttype['/=']['int']['float'] = 'float'
ttype['/=']['float']['int'] = 'float'

ttype['.+']['vector']['vector'] = 'vector'
ttype['.+']['matrix']['matrix'] = 'matrix'

ttype['.-']['vector']['vector'] = 'vector'
ttype['.-']['matrix']['matrix'] = 'matrix'

ttype['.*']['vector']['vector'] = 'vector'
ttype['.*']['matrix']['matrix'] = 'matrix'

ttype['./']['vector']['vector'] = 'vector'
ttype['./']['matrix']['matrix'] = 'matrix'

ttype['==']['int']['int'] = 'boolean'
ttype['==']['float']['float'] = 'boolean'
ttype['==']['int']['float'] = 'boolean'
ttype['==']['float']['int'] = 'boolean'
ttype['==']['string']['string'] = 'boolean'
ttype['==']['vector']['vector'] = 'boolean'
ttype['==']['matrix']['matrix'] = 'boolean'

ttype['!=']['int']['int'] = 'boolean'
ttype['!=']['float']['float'] = 'boolean'
ttype['!=']['int']['float'] = 'boolean'
ttype['!=']['float']['int'] = 'boolean'
ttype['!=']['string']['string'] = 'boolean'
ttype['!=']['vector']['vector'] = 'boolean'
ttype['!=']['matrix']['matrix'] = 'boolean'

ttype['>']['int']['int'] = 'boolean'
ttype['>']['float']['float'] = 'boolean'
ttype['>']['int']['float'] = 'boolean'
ttype['>']['float']['int'] = 'boolean'
ttype['>']['string']['string'] = 'boolean'

ttype['<']['int']['int'] = 'boolean'
ttype['<']['float']['float'] = 'boolean'
ttype['<']['int']['float'] = 'boolean'
ttype['<']['float']['int'] = 'boolean'
ttype['<']['string']['string'] = 'boolean'

ttype['>=']['int']['int'] = 'boolean'
ttype['>=']['float']['float'] = 'boolean'
ttype['>=']['int']['float'] = 'boolean'
ttype['>=']['float']['int'] = 'boolean'
ttype['>=']['string']['string'] = 'boolean'

ttype['<=']['int']['int'] = 'boolean'
ttype['<=']['float']['float'] = 'boolean'
ttype['<=']['int']['float'] = 'boolean'
ttype['<=']['float']['int'] = 'boolean'
ttype['<=']['string']['string'] = 'boolean'

ttype['unary']['int'][None] = 'int'
ttype['unary']['float'][None] = 'float'
ttype['unary']['vector'][None] = 'vector'
ttype['unary']['matrix'][None] = 'matrix'

ttype['transpose']['vector'][None] = 'matrix'
ttype['transpose']['matrix'][None] = 'matrix'