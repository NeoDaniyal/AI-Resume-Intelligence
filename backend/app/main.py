from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mongodb import connect_to_mongodb, close_mongodb_connection
from app.database.collections import initialize_collections


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Setup: Connect to MongoDB and initialize collections
    connect_to_mongodb()
    initialize_collections()
    yield

    #Shutdown: Close MongoDB connection
    close_mongodb_connection()

app = FastAPI(
    title="AI Resume Intelligence API",
    description="This API provides endpoints for AI-powered resume analysis and intelligence.",
    version="1.0.0",
    lifespan=lifespan
)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Resume Intelligence API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "AI Resume Intelligence"}

@app.get("/database-health")
def database_health_check():
    from app.database.mongodb import get_database
    db = get_database()
    return {"status": "healthy", "service": "Database"}