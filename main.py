from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "message": "Welcome to your assistant backend!" }

@app.get("/hello")
def say_hello(name: str = "Guest"):
    return { "message": f"Hello, {name}!" }