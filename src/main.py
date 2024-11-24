from fastapi import FastAPI
from src.routes.tasks import router as tasks_router
from src.routes.health import router as health_router

app = FastAPI()
app.include_router(tasks_router, prefix="/api/v1")
app.include_router(health_router, prefix="/api/v1")


@app.get("/")
def read_root(name: str = "User"):
    return {
        "message": f"🎉 Welcome, {name}! Your assistant backend is up and running! 🚀"
    }
