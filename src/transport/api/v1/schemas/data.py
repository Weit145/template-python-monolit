import datetime
import uuid
from enum import StrEnum
from typing import Any
from urllib.parse import urlsplit

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, IPvAnyAddress, field_validator


class HTTPMethod(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    CONNECT = "CONNECT"


class Data(BaseModel):
    pass

class Log(BaseModel):
    ip: IPvAnyAddress = Field(..., description="IP address of the client")
    method: HTTPMethod = Field(..., description="HTTP method")
    uri: str = Field(..., min_length=1, max_length=2000, description="Request URI")
    status_code: int = Field(..., ge=100, le=599, description="HTTP status code")

    @field_validator("uri")
    @classmethod
    def validate_uri(cls, value: str) -> str:
        for char in value:
            if char.isspace():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or parsed.fragment or not parsed.path.startswith("/"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return value


class CreateData(Data):
    log: Log = Field(..., description="Log data", examples=["192.168.1.1 GET /api/users 200"])

    @field_validator("log", mode="before")
    @classmethod
    def parse_log(cls, value: Any) -> Any:
        if not isinstance(value, str):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        parts = value.split()
        if len(parts) != 4:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        ip, method, uri, status_code = parts
        return {
            "ip": ip,
            "method": method,
            "uri": uri,
            "status_code": status_code,
        }



class OutData(Data):
    id: uuid.UUID
    created: datetime.datetime
    log: Log
