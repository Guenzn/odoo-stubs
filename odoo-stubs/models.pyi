from . import api, fields
from collections import MutableMapping
from typing import Any, Optional, List, Union, Sequence, Tuple, Dict, Generator

SearchDomain = List[Union[str, Sequence[str]]]
RecordValue = Dict[str, Any]

regex_order: Any
regex_object_name: Any
regex_pg_name: Any
regex_field_agg: Any
AUTOINIT_RECALCULATE_STORED_FIELDS: int

def check_object_name(name: Any): ...
def raise_on_invalid_object_name(name: Any) -> None: ...
def check_pg_name(name: Any) -> None: ...

regex_private: Any

def check_method_name(name: Any) -> None: ...
def same_name(f: Any, g: Any): ...
def fix_import_export_id_paths(fieldname: Any): ...

class MetaModel(api.Meta):
    module_to_models: Any = ...
    def __init__(self, name: Any, bases: Any, attrs: Any) -> None: ...

class NewId:
    ref: Any = ...
    def __init__(self, ref: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    __nonzero__: Any = ...

IdType: Any
PREFETCH_MAX: int
LOG_ACCESS_COLUMNS: Any
MAGIC_COLUMNS: Any
VALID_AGGREGATE_FUNCTIONS: Any

class BaseModel:
    _id: int
    _name: str
    _description: str
    _sql_constraints: List
    _inherit: List[str]
    _inherits: Dict[str, str]
    _rec_name: str
    _order: str
    _context: Dict
    _fields: Dict[str, fields.Field]
    env: api.Environment
    CONCURRENCY_CHECK_FIELD: str = ...
    def view_init(self, fields_list: Any) -> None: ...
    def compute_concurrency_field(self) -> None: ...
    def compute_concurrency_field_with_access(self) -> None: ...
    def __new__(cls) -> None: ...
    def __init__(self, pool: Any, cr: Any) -> None: ...
    def export_data(self, fields_to_export: Any, raw_data: bool = ...): ...
    def load(self, fields: Any, data: Any): ...
    def default_get(self, fields_list: List[str]) -> Dict[str, Any]: ...
    def fields_get_keys(self): ...
    def view_header_get(self, view_id: Optional[Any] = ..., view_type: str = ...): ...
    def user_has_groups(self, groups: Any): ...
    def load_views(self, views: Any, options: Optional[Any] = ...): ...
    def fields_view_get(self, view_id: Optional[Any] = ..., view_type: str = ..., toolbar: bool = ..., submenu: bool = ...): ...
    def get_formview_id(self, access_uid: Optional[Any] = ...): ...
    def get_formview_action(self, access_uid: Optional[Any] = ...): ...
    def get_access_action(self, access_uid: Optional[Any] = ...): ...
    def search_count(self, args: Any) -> int: ...
    def search(self, args: SearchDomain, offset: int = ..., limit: Optional[int] = ..., order: Optional[str] = ..., count: bool = ...) -> BaseModel: ...
    def name_get(self) -> List[Tuple[int, str]]: ...
    def name_create(self, name: Any): ...
    def name_search(self, name: str = ..., args: Optional[Any] = ..., operator: str = ..., limit: int = ...): ...
    @classmethod
    def clear_caches(cls) -> None: ...
    def read_group(self, domain: Any, fields: Any, groupby: Any, offset: int = ..., limit: Optional[Any] = ..., orderby: bool = ..., lazy: bool = ...) -> List[Dict]: ...
    def init(self) -> None: ...
    def fields_get(self, allfields: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def get_empty_list_help(self, help: Any): ...
    def check_field_access_rights(self, operation: Any, fields: Any): ...
    def read(self, fields: Optional[List[str]] = ..., load: str = ...) -> List[Dict[str, Any]]: ...
    def get_metadata(self): ...
    def check_access_rights(self, operation: Any, raise_exception: bool = ...): ...
    def check_access_rule(self, operation: Any) -> None: ...
    def unlink(self): ...
    def write(self, vals: Any): ...
    def create(self, vals_list: Union[RecordValue, List[RecordValue]]): ...
    def copy_data(self, default: Optional[Any] = ...): ...
    def copy_translations(old: Any, new: Any, excluded: Any = ...): ...
    def copy(self, default: Optional[Any] = ...) -> BaseModel: ...
    def exists(self) -> BaseModel: ...
    def get_external_id(self) -> Dict[int, str]: ...
    get_xml_id: Any = ...
    @classmethod
    def is_transient(cls): ...
    def resolve_2many_commands(self, field_name: Any, commands: Any, fields: Optional[Any] = ...): ...
    resolve_o2m_commands_to_record_dicts: Any = ...
    def search_read(self, domain: Optional[Any] = ..., fields: Optional[Any] = ..., offset: int = ..., limit: Optional[Any] = ..., order: Optional[Any] = ...): ...
    def toggle_active(self) -> None: ...
    def browse(self, arg: Optional[Any] = ..., prefetch: Optional[Any] = ...) -> BaseModel: ...
    @property
    def ids(self) -> List[int]: ...
    def ensure_one(self): ...
    def with_env(self, env: Any) -> BaseModel: ...
    def sudo(self, user: Any = ...) -> BaseModel: ...
    def with_context(self, *args: Any, **kwargs: Any) -> BaseModel: ...
    def with_prefetch(self, prefetch: Optional[Any] = ...) -> BaseModel: ...
    def mapped(self, func: Any): ...
    def filtered(self, func: Any) -> BaseModel: ...
    def sorted(self, key: Optional[Any] = ..., reverse: bool = ...) -> BaseModel: ...
    def update(self, values: RecordValue) -> None: ...
    def new(self, values: RecordValue = ..., ref: Optional[Any] = ...) -> BaseModel: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any = ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[BaseModel]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __add__(self, other: Any) -> BaseModel: ...
    def concat(self, *args: Any) -> BaseModel: ...
    def __sub__(self, other: Any) -> BaseModel: ...
    def __and__(self, other: Any) -> BaseModel: ...
    def __or__(self, other: Any) -> BaseModel: ...
    def union(self, *args: Any) -> BaseModel: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __int__(self): ...
    def __hash__(self): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any): ...
    def refresh(self) -> None: ...
    def invalidate_cache(self, fnames: Optional[Any] = ..., ids: Optional[Any] = ...): ...
    def modified(self, fnames: Any) -> None: ...
    def recompute(self) -> None: ...
    def onchange(self, values: Any, field_name: Any, field_onchange: Any): ...

class RecordCache(MutableMapping):
    def __init__(self, record: Any) -> None: ...
    def __contains__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def __delitem__(self, name: Any) -> None: ...
    def __iter__(self) -> None: ...
    def __len__(self): ...
    def has_value(self, name: Any): ...
    def get_value(self, name: Any, default: Optional[Any] = ...): ...
    def set_special(self, name: Any, getter: Any) -> None: ...
    def set_failed(self, names: Any, exception: Any) -> None: ...
AbstractModel = BaseModel

class Model(AbstractModel): ...
class TransientModel(Model): ...

def itemgetter_tuple(items: Any): ...
def convert_pgerror_not_null(model: Any, fields: Any, info: Any, e: Any): ...
def convert_pgerror_unique(model: Any, fields: Any, info: Any, e: Any): ...

PGERROR_TO_OE: Any

def lazy_name_get(self): ...
