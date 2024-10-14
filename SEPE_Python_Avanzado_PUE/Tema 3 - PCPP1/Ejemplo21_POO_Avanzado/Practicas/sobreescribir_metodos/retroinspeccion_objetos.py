"""https://peps.python.org/pep-3119/#overloading-isinstance-and-issubclass

class ABCMeta(type):

    def __instancecheck__(cls, inst):
        '''Implement isinstance(inst, cls).'''
        return any(cls.__subclasscheck__(c)
                   for c in {type(inst), inst.__class__})

    def __subclasscheck__(cls, sub):
        '''Implement issubclass(sub, cls).'''
        candidates = cls.__dict__.get("__subclass__", set()) | {cls}
        return any(c in candidates for c in sub.mro())

class Sequence(metaclass=ABCMeta):
    __subclass__ = {list, tuple}

assert issubclass(list, Sequence)
assert issubclass(tuple, Sequence)

class AppendableSequence(Sequence):
    __subclass__ = {list}

assert issubclass(list, AppendableSequence)
assert isinstance([], AppendableSequence)

assert not issubclass(tuple, AppendableSequence)
assert not isinstance((), AppendableSequence)
"""


class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio


class ABCMeta(type):

    def __instancecheck__(cls, inst):
        print("Sobreescrito")
        return any(cls.__subclasscheck__(c)
                   for c in {type(inst), inst.__class__})

    def __subclasscheck__(cls, sub):
        print("Sobreescrito")
        candidates = cls.__dict__.get("__subclass__", set()) | {cls}
        return any(c in candidates for c in sub.mro())


class Sequence(metaclass=ABCMeta):
    __subclass__ = {list, tuple, dict, set, str, Producto}


class AppendableSequence(Sequence):
    __subclass__ = {Producto, list}


p1 = Producto(1, "Pantalla", 129.50)
print("-" * 5)
print(issubclass(Producto, Sequence))
print(isinstance(p1, Sequence))

print("-" * 5)
print(isinstance([], Sequence))
print(isinstance(list(), Sequence))
print(isinstance("fsdfdsfsd", Sequence))
print(isinstance(34654645, Sequence))

print("-" * 5)
print(isinstance(p1, AppendableSequence))

print("-" * 5)
print(isinstance([], AppendableSequence))
print(isinstance(list(), AppendableSequence))
