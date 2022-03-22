from fastapi import FastAPI
from typing import Optional
from shodan import Shodan
from colorama import init


app = FastAPI()

@app.get("/ip/{ip}")
async def get_ip(ip: str, key: Optional[str] = None):
    if key is None:
        return {"Error": "Please provide a valid API key"}
    else:
        try:
            api = Shodan(key)
            res = api.host(ip)
            return {
                "long": res["longitude"],
                "lat": res["latitude"],
            }
        except Exception as e:
            return {"Error": str(e)}

async def read_root():
    return [{"Hello": "World"},
           {"Hello2": "World2"},
           {"Hello2": "World2"}]

def get_items():
    {"id":1,"description": "Item 1"}

if __name__ == '__main__':
    init()
    uvicorn.run(app,host="127.0.0.1", port=8000)

#lancement du werver uvicorn webserv:app --reload