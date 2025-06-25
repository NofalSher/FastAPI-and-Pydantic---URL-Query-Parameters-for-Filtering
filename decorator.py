
def add_sprinkles(func):
    def wrapper():
        func()
        return wrapper


@add_sprinkles
def get_ice_cream():
    print("Getting ice cream...")
    
    
get_ice_cream()