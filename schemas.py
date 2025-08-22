from pydantic import BaseModel
from typing import List, Optional

# ----- USERS -----
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    bio: Optional[str] = None
    location: Optional[str] = None
    availability: Optional[str] = None
    skills: List[str] = []

    class Config:
        orm_mode = True

# ----- SKILLS -----
class SkillBase(BaseModel):
    name: str
    category: str

class SkillCreate(SkillBase):
    pass

class SkillOut(SkillBase):
    id: int
    class Config:
        orm_mode = True

# ----- SWAPS -----
class SwapBase(BaseModel):
    requester_id: int
    receiver_id: int
    skill_offered: str
    skill_requested: str

class SwapOut(SwapBase):
    id: int
    status: str
    class Config:
        orm_mode = True

# ----- REVIEWS -----
class ReviewBase(BaseModel):
    reviewer_id: int
    rating: int
    comment: Optional[str] = None

class ReviewOut(ReviewBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True
# ... your existing schemas above ...

# ----- TOKENS -----
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    sub: Optional[str] = None
