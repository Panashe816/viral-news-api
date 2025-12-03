from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://universalnews_user:V5niNC00UBFDXwyOvFJhCLjiYHFXZi8b@dpg-d4a28v7diees73cr0bm0-a.virginia-postgres.render.com/universalnews"
engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "Viral News API is running"}

@app.get("/news")
def get_news():
    query = text("""
        SELECT 
            id,
            title,
            content,
            image_url,
            category,
            created_at,
            source_url
        FROM articles
        ORDER BY created_at DESC
        LIMIT 50
    """)
    
    with engine.connect() as conn:
        rows = conn.execute(query).fetchall()

    results = []
    for r in rows:
        results.append({
            "id": r.id,
            "title": r.title,
            "content": r.content,
            "image_url": r.image_url,
            "category": r.category,
            "created_at": str(r.created_at),
            "source_url": r.source_url
        })
    
    return results
