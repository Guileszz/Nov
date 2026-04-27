from fastapi import FastAPI, Request
import time

app = FastAPI(title="Nov Predictive Observer")

@app.post("/observe")
async def observe(data: dict):
    print(f"[NOV] Observing telemetry: {data}")
    # Simple anomaly detection: if rating is low
    rating = data.get("rating", 5)
    if rating < 3:
        print(f"[NOV] ANOMALY DETECTED: Low rating {rating}")
        # In the future, this would signal PROJETS
    return {"status": "observed", "timestamp": time.time()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
