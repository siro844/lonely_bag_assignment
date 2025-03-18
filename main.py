
from fastapi import FastAPI
from endpoints.user import router as user_router

app=FastAPI()
app.include_router(user_router,prefix='/users')

@app.get('/')
async def health():
    return {"message":"Server is running"}