import uvicorn
from fastapi import FastAPI

from Views.computetime import Computetime

app = FastAPI()


@app.get("/datetime/datetimecompute")
async def datetimecompute():
    datetime = Computetime().date_days_count()

    return datetime


# if __name__ == '__main__':
#     uvicorn.run(app='app', host="127.0.0.1", port=8008, reload=True, debug=True)
