from pydantic import BaseModel, Field


class Stats(BaseModel):
    methods: dict[str, int] = Field(..., description="HTTP request counts grouped by method")
    status_codes: dict[str, int] = Field(..., description="HTTP request counts grouped by status code")
