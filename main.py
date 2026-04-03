from fastapi import FastAPI, Body
from agent import handle_act
app = FastAPI(title="autoppia-ultra-storm")
@app.post("/act")
async def act(p: dict = Body(...)): return {"actions": await handle_act(**p)}
