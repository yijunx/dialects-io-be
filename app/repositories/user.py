import uuid
from datetime import datetime, timezone

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.auth.core import Actor
from app.models.exceptions.base import CustomError
from app.models.schemas.user import User, UserCreate, UserGetParam, UserRoleEnum, Wink
from app.models.schemas.utils import PaginatedResponse
from app.models.sqlalchemy import UserRecord
from app.repositories.util import translate_query_pagination


class SqlAlchemyUserRepo:
    def __init__(self, db: Session, master_acc_email: str) -> None:
        self.db = db
        self.master_acc_email = master_acc_email

    def upsert_user(self, actor: Actor) -> Wink:
        """used by the login endpoint, login endpoint will get the
        id token from the idp. the frontend nextjs app should already
        verified the idtoken. thus the idtoken here must be legit.
        """
        db_user: UserRecord = (
            self.db.query(UserRecord).filter(UserRecord.email == actor.email).first()
        )

        if db_user:
            role = db_user.role
            previous_login_at = db_user.last_login_time
            # update stuff
            db_user.last_login_time = datetime.now(timezone.utc)
            db_user.realm = actor.iss.split("/")[-1]
        else:
            previous_login_at = None
            role = UserRoleEnum.reader
            db_user = UserRecord(
                id=actor.id,
                display_name=actor.name,
                email=actor.email,
                role=role,
                # created_at=datetime.now(timezone.utc),
                # updated_at=datetime.now(timezone.utc),
                # last_login_at=datetime.now(timezone.utc),
                realm=actor.iss.split("/")[-1],
            )
            self.db.add(db_user)
            self.db.flush()
        if actor.email == self.master_acc_email:
            role = UserRoleEnum.admin
        return Wink(
            last_login_at=previous_login_at, role=role, realm=actor.iss.split("/")[-1]
        )

    def create_user(self, user_create: UserCreate) -> User:
        db_user = UserRecord(
            id=uuid.uuid4(),
            display_name=user_create.display_name,
            email=user_create.email,
            role=user_create.role,
        )
        self.db.add(db_user)
        self.db.flush()
        return User.model_validate(db_user, from_attributes=True)

    def get_user(self, user_id: str) -> User:
        db_user: UserRecord = (
            self.db.query(UserRecord).filter(UserRecord.id == user_id).first()
        )
        if db_user:
            return User.model_validate(db_user, from_attributes=True)
        else:
            raise CustomError(status_code=404, message="User does not exist")

    def list_users(self, param: UserGetParam) -> PaginatedResponse[User]:
        query = self.db.query(UserRecord)

        if param.email:
            # email for exact match..
            query = query.filter(UserRecord.email == param.email)
        else:
            if param.name:
                query = query.filter(UserRecord.display_name.ilike(f"%{param.name}%"))

        total = query.count()
        limit, offset, paging = translate_query_pagination(
            total=total, query_param=param
        )
        db_items = query.limit(limit).offset(offset)

        return PaginatedResponse[User](
            data=[User.model_validate(x, from_attributes=True) for x in db_items],
            paging=paging,
        )
