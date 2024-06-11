from app.dao.base_dao import DAO
from app.db.models import User


class UserDAO(DAO):
    model = User
