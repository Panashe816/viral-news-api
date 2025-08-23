# models.py
from sqlalchemy import Column, Integer, Text, DateTime, Boolean
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    category = Column(Text)
    content = Column(Text)
    created_at = Column(DateTime)

class Headline(Base):
    __tablename__ = "headlines"

    id = Column(Integer, primary_key=True, index=True)
    headline = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    source = Column(Text)
    url = Column(Text)
    published_at = Column(DateTime)
    created_at = Column(DateTime)
    generated = Column(Boolean)