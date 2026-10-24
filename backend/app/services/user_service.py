from re import U
from app.utils.password import verify_password, hash_password
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest, PasswordUpdateRequest
from sqlalchemy.orm import Session
from app.common.exceptions import BusinessException


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


def update_password(db: Session, user: User, data: PasswordUpdateRequest):
    """修改密码"""
    if not verify_password(data.old_password, user.password):
        raise BusinessException(message="原密码错误")
    if data.old_password == data.new_password:
        raise BusinessException(message="新密码不能与原密码相同")
    user.password = hash_password(data.new_password)
    db.commit()


from operator import or_
from sqlalchemy.orm import Session
from app.common.response import PageResponse
from app.schemas.user import UserResponse


def get_user_page_list(
    db: Session, page: int, page_size: int, keywords: str | None = None
):
    # select * from user where username like '%张%' or name like '%张%';
    query = db.query(User)
    if keywords:
        query = query.filter(
            or_(User.username.ilike(f"%{keywords}%"), User.name.ilike(f"%{keywords}%"))
        )
    total = query.count()
    items = (
        query.order_by(User.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return PageResponse(
        list=[UserResponse.model_validate(item) for item in items], total=total
    )
