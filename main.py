from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/omikuji")
def omikuji():
    result = random.choice(
        ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    )
    return {"result": result}