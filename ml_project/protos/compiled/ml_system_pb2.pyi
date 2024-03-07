from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthCheckOutout(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class JobExecutionInput(_message.Message):
    __slots__ = ("model_content",)
    MODEL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    model_content: str
    def __init__(self, model_content: _Optional[str] = ...) -> None: ...

class JobExecutionOutput(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class ActionInput(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: str
    def __init__(self, action: _Optional[str] = ...) -> None: ...

class ActionOutput(_message.Message):
    __slots__ = ("acknowledgement", "checksum")
    ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    acknowledgement: str
    checksum: bytes
    def __init__(self, acknowledgement: _Optional[str] = ..., checksum: _Optional[bytes] = ...) -> None: ...
