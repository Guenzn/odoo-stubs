from .cache import *
import pickle as pickle_
import xlsxwriter
import xlwt
from . import pycompat as pycompat
from .config import config as config
from .parse_version import parse_version as parse_version
from .which import which as which
from collections import Mapping, MutableMapping, MutableSet, defaultdict
from itertools import repeat as repeat
from odoo.loglevels import exception_to_unicode as exception_to_unicode, get_encodings as get_encodings, ustr as ustr
from typing import Any, Optional

_logger: Any
SKIPPED_ELEMENT_TYPES: Any

def find_in_path(name: Any): ...
def _exec_pipe(prog: Any, args: Any, env: Optional[Any] = ...): ...
def exec_command_pipe(name: Any, *args: Any): ...
def find_pg_tool(name: Any): ...
def exec_pg_environ(): ...
def exec_pg_command(name: Any, *args: Any) -> None: ...
def exec_pg_command_pipe(name: Any, *args: Any): ...
def file_open(name: Any, mode: str = ..., subdir: str = ..., pathinfo: bool = ...): ...
def _fileopen(path: Any, mode: Any, basedir: Any, pathinfo: Any, basename: Optional[Any] = ...): ...
def flatten(list: Any): ...
def reverse_enumerate(l: Any): ...
def partition(pred: Any, elems: Any): ...
def topological_sort(elems: Any): ...

class PatchedWorkbook(xlwt.Workbook):
    def add_sheet(self, name: Any, cell_overwrite_ok: bool = ...): ...

class PatchedXlsxWorkbook(xlsxwriter.Workbook):
    def add_worksheet(self, name: Optional[Any] = ..., **kw: Any): ...

def to_xml(s: Any): ...
def get_iso_codes(lang: Any): ...
def scan_languages(): ...
def get_user_companies(cr: Any, user: Any): ...
def mod10r(number: Any): ...
def str2bool(s: Any, default: Optional[Any] = ...): ...
def human_size(sz: Any): ...
def logged(f: Any): ...

class profile:
    fname: Any = ...
    def __init__(self, fname: Optional[Any] = ...) -> None: ...
    def __call__(self, f: Any): ...

def detect_ip_addr(): ...

DEFAULT_SERVER_DATE_FORMAT: str
DEFAULT_SERVER_TIME_FORMAT: str
DEFAULT_SERVER_DATETIME_FORMAT: Any
DATE_LENGTH: Any
DATETIME_FORMATS_MAP: Any
POSIX_TO_LDML: Any

def posix_to_ldml(fmt: Any, locale: Any): ...
def split_every(n: Any, iterable: Any, piece_maker: Any = ...) -> None: ...
def get_and_group_by_field(cr: Any, uid: Any, obj: Any, ids: Any, field: Any, context: Optional[Any] = ...): ...
def get_and_group_by_company(cr: Any, uid: Any, obj: Any, ids: Any, context: Optional[Any] = ...): ...
def resolve_attr(obj: Any, attr: Any): ...
def attrgetter(*items: Any): ...
def remove_accents(input_str: Any): ...

class unquote(str):
    def __repr__(self): ...

class UnquoteEvalContext(defaultdict):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __missing__(self, key: Any): ...

class mute_logger:
    loggers: Any = ...
    def __init__(self, *loggers: Any) -> None: ...
    def filter(self, record: Any): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Optional[Any] = ..., exc_val: Optional[Any] = ..., exc_tb: Optional[Any] = ...) -> None: ...
    def __call__(self, func: Any): ...

_ph: Any

class CountingStream:
    stream: Any = ...
    index: Any = ...
    stopped: bool = ...
    def __init__(self, stream: Any, start: int = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def next(self): ...
    __next__: Any = ...

def stripped_sys_argv(*strip_args: Any): ...

class ConstantMapping(Mapping):
    __slots__: Any = ...
    _value: Any = ...
    def __init__(self, val: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, item: Any): ...

def dumpstacks(sig: Optional[Any] = ..., frame: Optional[Any] = ..., thread_idents: Optional[Any] = ...) -> None: ...
def freehash(arg: Any): ...
def clean_context(context: Any): ...

class frozendict(dict):
    def __delitem__(self, key: Any) -> None: ...
    def __setitem__(self, key: Any, val: Any) -> None: ...
    def clear(self) -> None: ...
    def pop(self, key: Any, default: Optional[Any] = ...) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, key: Any, default: Optional[Any] = ...) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def __hash__(self) -> Any: ...

class Collector(Mapping):
    __slots__: Any = ...
    _map: Any = ...
    def __init__(self) -> None: ...
    def add(self, key: Any, val: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...

class StackMap(MutableMapping):
    __slots__: Any = ...
    _maps: Any = ...
    def __init__(self, m: Optional[Any] = ...) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, val: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def __str__(self): ...
    def pushmap(self, m: Optional[Any] = ...) -> None: ...
    def popmap(self): ...

class OrderedSet(MutableSet):
    __slots__: Any = ...
    _map: Any = ...
    def __init__(self, elems: Any = ...) -> None: ...
    def __contains__(self, elem: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def add(self, elem: Any) -> None: ...
    def discard(self, elem: Any) -> None: ...

class LastOrderedSet(OrderedSet):
    def add(self, elem: Any) -> None: ...

def groupby(iterable: Any, key: Optional[Any] = ...): ...
def unique(it: Any) -> None: ...

class Reverse:
    __slots__: Any = ...
    val: Any = ...
    def __init__(self, val: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...

def ignore(*exc: Any) -> None: ...
def html_escape(text: Any): ...
def formatLang(env: Any, value: Any, digits: Optional[Any] = ..., grouping: bool = ..., monetary: bool = ..., dp: bool = ..., currency_obj: bool = ...): ...
def format_date(env: Any, value: Any, lang_code: bool = ..., date_format: bool = ...): ...
def _consteq(str1: Any, str2: Any): ...

consteq: Any

class Unpickler(pickle_.Unpickler):
    find_global: Any = ...
    find_class: Any = ...

def _pickle_load(stream: Any, encoding: str = ..., errors: bool = ...): ...

pickle: Any

def wrap_module(module: Any, attr_list: Any): ...

class DotDict(dict):
    def __getattr__(self, attrib: Any): ...

def traverse_containers(val: Any, type_: Any) -> None: ...
