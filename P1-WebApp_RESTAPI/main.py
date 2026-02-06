from fastapi import FastAPI

app = FastAPI()

posts = [
    {
        "id":1,
        "title":"Title 1"
    },
    {
        "id":2,
        "title":"Title 2"
    },
]


@app.get("/")
def home():
    return {"message":"Hello World"}


@app.get("/api/posts",include_in_schema=False)
@app.get("/posts")
def get_post():
    return posts