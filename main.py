from fastapi import FastAPI

from controllers.post import router as postapi
from controllers.feed import router as feedapi
from controllers.search import router as searchapi
from controllers.login import app as loginapi
from controllers.likeShare import router as likeapis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
origins = ["*"]

# Add CORS middleware to handle OPTIONS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify the allowed HTTP methods here
    allow_headers=["*"],  # You can specify the allowed headers here
)
app.include_router(postapi)
app.include_router(feedapi)
app.include_router(searchapi)
app.include_router(loginapi)
app.include_router(likeapis)


@app.get("/")
async def health_check():

    return {"Message": "To access APIs put /docs in the URL."}
# If this script is executed, run the FastAPI application directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)