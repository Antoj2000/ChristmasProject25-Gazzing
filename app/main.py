from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from .schemas import DepotResolveRequest, DepotResolveResponse
from .service import DepotService

app = FastAPI()

@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/depot/{area}", response_model=DepotResolveResponse)
def get_depot(area: str):
    try:
        result = DepotService.get_depot_from_area(area)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/api/depot", response_model=DepotResolveResponse)
def post_depot_lookup(payload: DepotResolveRequest):
    try:
        result = DepotService.get_depot_from_area(payload.addressline4)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    