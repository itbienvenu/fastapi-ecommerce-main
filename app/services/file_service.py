import os
import shutil
import uuid
from fastapi import UploadFile, HTTPException
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileService:
    @staticmethod
    async def upload_file(file: UploadFile) -> str:
        if not file.content_type.startswith("image/"):
            raise HTTPException(400, "Invalid file type. Only images are allowed.")

        file_extension = os.path.splitext(file.filename)[1]
        if not file_extension:
            file_extension = ".jpg"  # Default to jpg if no extension

        filename = f"{uuid.uuid4()}{file_extension}"
        file_path = UPLOAD_DIR / filename

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        except Exception as e:
            raise HTTPException(500, f"Could not save file: {str(e)}")

        return f"/static/{filename}"
