from pydantic import BaseModel
from typing import List, Optional


class ResponseList(BaseModel):
    code: int
    ok: bool
    msg: str
    error: str
    data: List = []


class ResponseDictionary(BaseModel):
    code: int
    ok: bool
    msg: str
    error: str
    data: Optional[dict] = None
