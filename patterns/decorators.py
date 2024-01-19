def singleton(cls):
    
    _instances = {}
    
    def wrap(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    
    return wrap