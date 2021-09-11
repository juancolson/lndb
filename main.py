from fastapi import FastAPI
from scraper import Search

app = FastAPI()
Searched = Search()

@app.get("/{search}")
async def read_item(search):
  return Searched.searcher(search)
