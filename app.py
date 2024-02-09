import aioredis

from dotenv import dotenv_values
from api.protocol import ChallengeRequest
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi import FastAPI, Request, HTTPException, Depends
from huggingface_hub import AsyncInferenceClient, InferenceClient

config = dotenv_values(".env")

app = FastAPI()
client = AsyncInferenceClient("http://127.0.0.1:8080")

REDIS_URL = config["REDIS_URL"]
REDIS_PORT = config["REDIS_PORT"]
REDIS_PASSWORD = config["REDIS_PASSWORD"]

@app.on_event("startup")
async def startup():
    redis_connection = aioredis.from_url(f"rediss://default:{REDIS_PASSWORD}@{REDIS_URL}:{REDIS_PORT}", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_connection)



@app.get("/", dependencies=[
    Depends(RateLimiter(times=10, seconds=5)),
    Depends(RateLimiter(times=3000, seconds=3600)),
])
async def root(request: Request):
    return {"message": "Hello World"}

@app.post("/", dependencies=[
    Depends(RateLimiter(times=1, seconds=12)),
    Depends(RateLimiter(times=600, seconds=3600)),
])
async def generate(request: ChallengeRequest):
    prompt = request.private_input
    sampling_params = request.sampling_params
    response = await client.text_generation(
        prompt=prompt,
        best_of=sampling_params.best_of,
        max_new_tokens=sampling_params.max_new_tokens,
        seed=sampling_params.seed,
        do_sample=sampling_params.do_sample,
        repetition_penalty=sampling_params.repetition_penalty,
        temperature=sampling_params.temperature,
        top_k=sampling_params.top_k,
        top_p=sampling_params.top_p,
        truncate=sampling_params.truncate,
        typical_p=sampling_params.typical_p,
        watermark=sampling_params.watermark,
    )
    return {"response": response}