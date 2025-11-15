# api.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Article  # Make sure you have Article model defined in models.py

Base.metadata.create_all(bind=engine)  # Creates tables if not exists

app = FastAPI(title="Viral News API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Viral News API is running"}

@app.get("/latest-articles")
def latest_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).order_by(Article.id.desc()).limit(10).all()
    return {"articles": [ {"id": a.id, "title": a.title, "content": a.content} for a in articles ]}
