
from fastapi import APIRouter, UploadFile, File, HTTPException
from datetime import datetime, timezone

from app.utils.file_validator import validate_file
from app.services.resume_parser import extract_text
from app.services.text_cleaner import clean_resume_text
from app.database.mongodb import get_database

router = APIRouter(
    prefix="/resumes",
    tags=["Resume Management"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    # Step 1: Validate file
    content = await validate_file(file)

    filename = file.filename.lower()
    extension = "." + filename.rsplit(".", 1)[-1]

    # Step 2: Extract text
    try:
        extracted_text = extract_text(
            content,
            extension
        )

    except Exception:
        raise HTTPException(
            status_code=422,
            detail="Unable to process the uploaded document."
        )

    # Step 3: Clean extracted text
    cleaned_text = clean_resume_text(
        extracted_text
    )

    if not cleaned_text:
        raise HTTPException(
            status_code=422,
            detail=(
                "No readable text found. "
                "The document may be scanned or empty."
            )
        )

    # Step 4: Store in MongoDB
    db = get_database()

    resume_data = {
        "user_id": None,
        "filename": file.filename,
        "file_type": extension.replace(".", ""),
        "file_size": len(content),
        "extracted_text": cleaned_text,
        "status": "uploaded",
        "created_at": datetime.now(timezone.utc)
    }

    result = db.resumes.insert_one(resume_data)

    # Step 5: Return response
    return {
        "message": "Resume uploaded successfully!",
        "resume_id": str(result.inserted_id),
        "filename": file.filename,
        "file_type": extension.replace(".", ""),
        "extracted_text": cleaned_text
    }
