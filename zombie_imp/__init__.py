from .imp_3_11 import *
from .imp_3_11 import _fix_co_filename
try:
    from .imp_3_11 import _frozen_module_names
except ImportError:
    pass
from .imp_3_11 import _ERR_MSG, _exec, _load, _builtin_from_name
from .imp_3_11 import _HackedGetData, _LoadSourceCompatibility, _LoadCompiledCompatibility
