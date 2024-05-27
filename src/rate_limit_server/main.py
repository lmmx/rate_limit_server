from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/api/resource1")
@limiter.limit("4/2 seconds")
async def read_resource1(request: Request):
    return {"message": "This is resource 1"}


@app.get("/api/resource2")
@limiter.limit("5/minute")
async def read_resource2(request: Request):
    return {"message": "This is resource 2"}


def run_app():
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
