from pydantic import BaseModel


class Request(BaseModel):
    driver: str
    zpl: str
