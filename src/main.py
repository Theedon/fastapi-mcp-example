import json
from pathlib import Path

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from src.router import calc, google_calendar, google_tasks

app = FastAPI()

app.include_router(google_tasks.router, prefix="/google_tasks")
app.include_router(google_calendar.router, prefix="/google_calendar")
app.include_router(calc.router, prefix="/calc")

mcp = FastApiMCP(app)

mcp.mount()


@app.get("/status")
def status():
    return {"status": "ok"}


@app.get("/metadata")
def metadata():
    return {
        "name": "Multi-tool MCP Server",
        "description": "Tools for Google Tasks, Calendar, and Instagram",
    }


@app.get("/openapi.json")
def openapi():
    with open(Path(__file__).parent / "openapi.json") as f:
        return json.load(f)
