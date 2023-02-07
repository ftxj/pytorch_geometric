import os
import os.path as osp
import sys
from getpass import getuser
from importlib.util import module_from_spec, spec_from_file_location
from tempfile import NamedTemporaryFile as TempFile
from tempfile import gettempdir

from torch_geometric.data.makedirs import makedirs

base_dir = os.getcwd()
def class_from_module_repr(access_name, cls_name, module_repr):
    with open(osp.join(base_dir, cls_name + ".py"), mode='w') as f:
        f.write(module_repr)
    spec = spec_from_file_location(cls_name, f.name)
    mod = module_from_spec(spec)
    sys.modules[cls_name] = mod
    spec.loader.exec_module(mod)
    return getattr(mod, access_name)
