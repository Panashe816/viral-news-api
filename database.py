# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path

# Get the path to the directory where this script is located
script_dir = Path(__file__).parent

# Load environment variables from the .env file in the SAME directory as this script
env_path = script_dir / '.env'
load_dotenv(env_path)

# 1. Get the complete DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Debug: Check if the .env file is being loaded
if DATABASE_URL is None:
    print(f"❌ ERROR: DATABASE_URL not found in environment variables!")
    print(f"Looking for .env file at: {env_path}")
    print(f".env file exists: {env_path.exists()}")
    
    if env_path.exists():
        print("Contents of .env file:")
        with open(env_path, 'r') as f:
            print(f.read())
    
    # For now, let's hardcode the URL for testing
    DATABASE_URL = "postgresql://viraluser:7HCll7FgeovB70iU0d72ISLbo6F8DfyB@dpg-d28cf2euk2gs73f5bs4g-a.virginia-postgres.render.com/viralnews"
    print("Using hardcoded DATABASE_URL for now...")
else:
    print("✅ Successfully loaded DATABASE_URL from .env file!")

# 2. Create the SQLAlchemy Engine for PostgreSQL
try:
    engine = create_engine(
        DATABASE_URL,
        connect_args={
            "sslmode": "require"  # This is crucial for Render.com PostgreSQL
        },
        echo=False  # Set to True to see SQL queries in console (helpful for debugging)
    )
    print("✅ Database engine created successfully!")
except Exception as e:
    print(f"❌ Failed to create database engine: {e}")
    raise

# 3. Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class for our models to inherit from (updated for SQLAlchemy 2.0)
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test the connection immediately
def test_connection():
    try:
        with engine.connect() as conn:
            print("✅ Successfully connected to the database!")
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

# Test connection when this module is run directly
if __name__ == "__main__":
    print("Testing database connection...")
    test_connection()
else:
    # Test connection when imported
    test_connection()

print("✅ Database module loaded successfully!")