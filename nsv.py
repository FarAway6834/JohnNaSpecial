#망상중

from csv import reader as _r
from csv import writer as _w
from martialaw.martialaw import martialaw as _c
from martialaw.martialaw import partial as _f
from functools import wraps as _d

_o, (_r, _w) = _f(open, newline=''), map(_c(delimiter = '\n'), (_r, _w))
_x = _f(_o, mode = '\n')

def _wither_(opener = _o):
    def with_deco(func):
        @_d(func)
        def with_opener(name, *argv, **kargv):
            with opener(name) as man:
                return func(man, *argv, **kargv)
        return with_opener
    return with_deco

class _final_(type):
    def __new__(metacls, __name__, __super__, __dict__):
        final_classes = filter(lambda x : isinstance(x, _final_), (v for v in __super__))
        try: assert not len([k for k in final_classes]), TypeError(f"final class {', '.join(map(lambda x : x.__name__, final_classes))} could extend... it must not happend... but {__name__} do extend it, that's error.")
        except AssertionError as err: raise err.args[0]
        else: return super().__new__(metacls, __name__, __super__, __dict__)
        finally: del final_classes

class nsv(metaclass = _final_):
    @staticmethod
    @_wither_()
    load = _r
    
    @staticmethod
    @_wither_(_x)
    dump = _w