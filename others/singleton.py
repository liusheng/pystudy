def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class Foo(object):
    a = 1

    def __init__(self, x=0):
        self.x = x
