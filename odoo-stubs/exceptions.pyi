from typing import Any, Optional

_logger: Any

class except_orm(Exception):
    name: Any = ...
    value: Any = ...
    args: Any = ...
    def __init__(self, name: Any, value: Optional[Any] = ...) -> None: ...

class UserError(except_orm):
    def __init__(self, msg: Any) -> None: ...
Warning = UserError

class RedirectWarning(Exception):
    @property
    def name(self): ...

class AccessDenied(Exception):
    __cause__: Any = ...
    traceback: Any = ...
    def __init__(self, message: str = ...) -> None: ...

class AccessError(except_orm):
    def __init__(self, msg: Any) -> None: ...

class CacheMiss(except_orm, KeyError):
    def __init__(self, record: Any, field: Any) -> None: ...

class MissingError(except_orm):
    def __init__(self, msg: Any) -> None: ...

class ValidationError(except_orm):
    def __init__(self, msg: Any) -> None: ...

class DeferredException(Exception):
    message: Any = ...
    traceback: Any = ...
    def __init__(self, msg: Any, tb: Any) -> None: ...

class QWebException(Exception): ...
