from fastapi import FastAPI, APIRouter

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root() -> dict:

    return {"msg": "Hwllo, World!"}

app.include_router(api_router)

if __name__=="__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")