from sqlalchemy import update as sql_update
from app.reposetory.base_r import BaseRepository
from app.config import db,commit_rollback
from sqlalchemy.future import select
from app.model.users import Users



class UsersReposetory(BaseRepository):
    model = Users

    @staticmethod
    async def find_by_username(username: str):
        query = select(Users).where(Users.username == username)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def find_by_email(email: str):
        query = select(Users).where(Users.email == email)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def update_password(email:str,password:str):
        query = sql_update(Users).where(email == email).values(
            password=password).execution_options(synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()







