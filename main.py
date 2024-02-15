from fastapi import FastAPI

from controllers.post import router as postapi
from controllers.feed import router as feedapi
from controllers.search import router as searchapi
from controllers.login import app as loginapi
from controllers.likeShareRe import router as likeapis
from controllers.profile import router as profileapis
from controllers.fileUpload import router as fileapis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
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
app.include_router(profileapis)
app.include_router(fileapis)



@app.get("/")
async def root():
    return {"message": "Hello World"}


# If this script is executed, run the FastAPI application directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)