from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://universalnews_user:V5niNC00UBFDXwyOvFJhCLjiYHFXZi8b@dpg-d4a28v7diees73cr0bm0-a.virginia-postgres.render.com/universalnews"

engine = create_engine(DATABASE_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Viral News API is running"}

@app.get("/news")
def get_news():
    query = text("""
        SELECT 
            id, 
            title, 
            headline, 
            article, 
            category, 
            created_at
        FROM articles
        ORDER BY created_at DESC
        LIMIT 50;
    """)
    
    with engine.connect() as conn:
        rows = conn.execute(query).fetchall()

    results = []
    for r in rows:
        results.append({
            "id": r.id,
            "title": r.title,
            "headline": r.headline,
            "article": r.article,
            "category": r.category,
            "created_at": str(r.created_at),
        })
    
    return results
