from fastapi import APIRouter, UploadFile, File, Depends
from app.services.file_service import FileService
from app.schema.common_schema import FileUploadResponse
from app.dependencies import require_admin
from app.schema.user_schema import UserPublic
from typing import Annotated

router = APIRouter(tags=["Upload"])


@router.post("", response_model=FileUploadResponse, summary="Upload a file")
async def upload_file(
    admin: Annotated[UserPublic, Depends(require_admin)],
    file: UploadFile = File(...),
):
    """
    Upload an image file. Only admins can upload files.
    """
    url = await FileService.upload_file(file)
    return {"url": url}
