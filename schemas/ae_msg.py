from pydantic import BaseModel


class MsgBase(BaseModel):
    category: str | None = None
    time: str | None = None
    content: str | None = None

class MsgCreate(MsgBase):
    pass


class Out(BaseModel):
    time: str | None = None   
    category: str | None = None
    code: str | None = None
    content: str | None = None

