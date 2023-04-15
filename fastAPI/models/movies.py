from config.database import Base
from sqlalchemy import Column, String, Integer


class Movie(Base):
    
    __tablename__ = "movies"
    
    id = Column(Integer, unique=True, primary_key=True)
    title = Column(String, unique=True)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(String)
    category = Column(String)