from re import U

from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest
from sqlalchemy.orm import Session


def get_user_info(user: User) -> UserResponse:
    return UserResponse.model_validate(user)


def update_user_info(db: Session, user: User, data: UserUpdateRequest):
    user_dict = data.model_dump(exclude_none=True)  # pydatic对象转换成字典
    for field, value in user_dict.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    # 类似于：
    # user.name = user.name
    # user.email = user.email
    # user.phone = user.phone
    # user.avatar = user.avatar
    return UserResponse.model_validate(user)
