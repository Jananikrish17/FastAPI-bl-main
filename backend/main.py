from fastapi import FaastAPI
from core.config import settings

app = FaastAPI(title =settings.PROJECT_TITLE, version =settings.PROJECT_VERSION)

@app.get("/")
def hello():
    return {"msg":"Hello World"}