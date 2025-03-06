from pydantic import BaseModel


class MsgBase(BaseModel):
    category: str | None = None
    time: str | None = None
    content: str | None = None

class MsgCreate(MsgBase):
    pass


class Out(BaseModel):
    res: str | None = None   
    content: str | None = None

