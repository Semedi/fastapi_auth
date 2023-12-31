from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import ecgs, users

app = FastAPI()

app.include_router(users.router)
app.include_router(ecgs.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

@app.get("/")
def read_root():
    return {"message": "Idoven test"}
