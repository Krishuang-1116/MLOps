from typing import Union
from prometheus_client import Counter, Histogram, start_http_server

from fastapi import FastAPI, Query
from pydantic import BaseModel
# Imports the scoring function from score.py
from assignment1.scoring import score_house_price

app = FastAPI()

# Define metrics and start the second port(8001) for monitoring performance metrics
# --- Metrics (second port: 8001) ---
REQUEST_COUNT = Counter("api_requests_total",
                        "Total number of requests to the API")
REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds", "Latency for API requests")


@app.on_event("startup")
def startup_event():
    # Start a separate HTTP server that exposes Prometheus metrics on port 8001
    start_http_server(8001)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # Call the scoring function
    score = score_house_price(item.name, item.price, item.is_offer)
    return {
        "item_name": item.name,
        "item_id": item_id,
        "score": score,
    }

@app.get("/apartment/v1/score")
def score_apartment(
    surface: float = Query(..., gt=0, description="Surface in m²"),
    rooms: int = Query(..., ge=0, description="Number of rooms"),
):
    """
    Teacher-style standardized endpoint:
    /apartment/v1/score?surface=...&rooms=...
    """
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        predicted_price = score_house_price(item_name="apartment", item_price=surface * 1000, is_offer=None)
    return {
        "version": "v1",
        "input": {"surface": surface, "rooms": rooms},
        "predicted_price": predicted_price,
    }
