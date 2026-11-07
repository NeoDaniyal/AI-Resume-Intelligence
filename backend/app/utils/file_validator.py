from fastapi import UploadFile, HTTPException

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {".pdf": "pdf", ".docx": "docx"}

async def validate_file(file: UploadFile):
    filename = (file.filename or "").lower()

    extension = "." + filename.split(".")[-1] if "." in filename else ""

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS.keys())}")

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="File is empty")

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail=f"File size exceeds the maximum limit of {MAX_FILE_SIZE / (1024 * 1024)} MB")

    if extension == ".pdf":
        valid_signature = content.startswith(b"%PDF-")
    else:
        valid_signature = content.startswith(b"PK\x03\x04")  # DOCX files are ZIP archives

    if not valid_signature:
        raise HTTPException(status_code=400, detail=f"File content does not match the expected format for {ALLOWED_EXTENSIONS[extension]} files")

    await file.seek(0)
    return content