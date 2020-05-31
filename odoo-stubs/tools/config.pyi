import optparse
from . import appdirs as appdirs, pycompat as pycompat
from .. import conf as conf, loglevels as loglevels, release as release
from typing import Any, Optional

crypt_context: Any

class MyOption(optparse.Option):
    my_default: Any = ...
    def __init__(self, *opts: Any, **attrs: Any) -> None: ...

DEFAULT_LOG_HANDLER: str

def _get_default_datadir(): ...
def _deduplicate_loggers(loggers: Any): ...

class configmanager:
    options: Any = ...
    blacklist_for_save: Any = ...
    casts: Any = ...
    misc: Any = ...
    config_file: Any = ...
    _LOGLEVELS: Any = ...
    parser: Any = ...
    def __init__(self, fname: Optional[Any] = ...) -> None: ...
    def parse_config(self, args: Optional[Any] = ...) -> None: ...
    rcfile: Any = ...
    def _parse_config(self, args: Optional[Any] = ...) -> None: ...
    def _is_addons_path(self, path: Any): ...
    def _check_addons_path(self, option: Any, opt: Any, value: Any, parser: Any) -> None: ...
    def _test_enable_callback(self, option: Any, opt: Any, value: Any, parser: Any) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def pop(self, key: Any, default: Optional[Any] = ...): ...
    def get_misc(self, sect: Any, key: Any, default: Optional[Any] = ...): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    @property
    def addons_data_dir(self): ...
    @property
    def session_dir(self): ...
    def filestore(self, dbname: Any): ...
    def set_admin_password(self, new_password: Any) -> None: ...
    def verify_admin_password(self, password: Any): ...

config: Any
