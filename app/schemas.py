# schemas.py
from pydantic import BaseModel, Field


class DepotResolveRequest(BaseModel):
    addressline4: str = Field()


class DepotResolveResponse(BaseModel):
    query: str
    normalised: str
    depot_number: int
