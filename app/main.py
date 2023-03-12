from fastapi import FastAPI,APIRouter
from config import db
import uvicorn


#Асинх Сессия мигриует с приложением
def init_app():
    db.init()
    app = FastAPI(
        title='Engine Viva',
        description="Login page",
        version="1"
    )

    @app.on_event('startup')
    async def startup():
        await db.create_all()


    @app.on_event('shutdown')
    async def shutdown():
        db.close()

    return app

app = init_app()

#автомат.сервер
if __name__ == '__main__':
    uvicorn.run('main:app',port=8000,host='0.0.0.0',reload=True)