from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Every person who joins our SkillSwap world
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    bio = Column(String, nullable=True)
    location = Column(String, nullable=True)
    availability = Column(String, nullable=True)

    # Connections
    skills = relationship("Skill", back_populates="owner")
    reviews = relationship("Review", back_populates="user")

# Skills are like "superpowers" users bring
class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="skills")

# A swap is like a handshake between two friends
class Swap(Base):
    __tablename__ = "swaps"

    id = Column(Integer, primary_key=True, index=True)
    requester_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    skill_offered = Column(String)
    skill_requested = Column(String)
    status = Column(String, default="pending")  # pending → accepted → done

# Reviews are the "thank you notes" after learning
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reviewer_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer)
    comment = Column(String, nullable=True)

    user = relationship("User", back_populates="reviews")

