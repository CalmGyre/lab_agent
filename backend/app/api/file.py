import os
import time
from pathlib import Path
import uuid
from fastapi import APIRouter, File, UploadFile

from app.common.exceptions import BusinessException
from app.common.response import Response
from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, UPLOAD_DIR
from app.schemas.file import FileResponse

router = APIRouter(prefix="/files", tags=["文件管理"])


@router.post("/upload")
def upload(file: UploadFile = File(...)):
    """文件上传的接口"""
    if not file.filename:
        raise BusinessException(message="文件名不能为空")

    # 原始的文件名  用户头像.jpg
    orignal_name = os.path.basename(file.filename)
    # 文件后缀 .jpg
    ext = Path(orignal_name).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise BusinessException(message=f"不支持的文件后缀：{ext}")
    # 文件大小校验
    if file.size is not None and file.size > MAX_FILE_SIZE:
        raise BusinessException(
            message=f"文件不能超过 {MAX_FILE_SIZE // 1024 // 1024}MB"
        )
    # 设置唯一的文件名称   199323213213_ddadaqwerq.jpg
    disk_name = f"{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}{ext}"
    # 文件存储的实际路径
    save_path = UPLOAD_DIR / disk_name

    # 流式写文件
    size = 0
    try:
        with open(save_path, "wb") as f:
            while chunk := file.file.read(1024 * 1024):
                size += len(chunk)
                if size > MAX_FILE_SIZE:
                    raise BusinessException(
                        message=f"文件不能超过 {MAX_FILE_SIZE // 1024 // 1024}MB"
                    )
                f.write(chunk)
    except Exception:
        save_path.unlink(missing_ok=True)
        raise

    return Response.success(
        data=FileResponse(
            original_name=orignal_name,
            disk_name=disk_name,
            size=size,
            url=f"/uploads/{disk_name}",
        )
    )
