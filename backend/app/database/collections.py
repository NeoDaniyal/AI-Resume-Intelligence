from app.database.mongodb import get_database

def initialize_collections():
    db = get_database()
    # Initialize your collections here if needed
    # For example, you can create indexes or perform other setup tasks
    collections = [
        "users",
        "resumes",
        "resume_versions",
        "job_descriptions",
        "analysis_results",
        "resume_templates",
    ]
    print("Collections initialized")
    existing = db.list_collection_names()

    for collection in collections:
        if collection not in existing:
            db.create_collection(collection)

    db.users.create_index("email", unique=True)
    db.resumes.create_index("user_id")
    db.resume_versions.create_index([("resume_id", 1), ("version_number", -1)], unique=True)
    db.job_descriptions.create_index("user_id")
    db.analysis_results.create_index("resume_id")

    print("Indexes created for collections")