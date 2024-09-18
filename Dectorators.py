def decorators(name):
    def wrap(*args,**kwargs):
        print(f"Before calling {name.__name__} function")
        print(name(*args,**kwargs))
        print(f"After calling {name.__name__} function")
    return wrap
@decorators
def Call(name):
    return f"Hi!! {name}"
Call("Leezhan")