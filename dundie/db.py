"""Database connection"""
from sqlmodel import create_engine
from .config import settings
from sqlmodel import Session

engine = create_engine(
    settings.db.uri,  # pyright: ignore
    echo=settings.db.echo,  # pyright: ignore
    connect_args=settings.db.connect_args,  # pyright: ignore
)

def get_db_session():
    """Get a new session"""
    with Session(engine) as session:
        yield session

