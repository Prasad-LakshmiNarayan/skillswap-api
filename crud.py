from sqlalchemy.orm import Session
import models, schemas

# ----- USERS -----
def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

# ----- SKILLS -----
def add_skill(db: Session, user_id: int, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.dict(), user_id=user_id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

# ----- SWAPS -----
def request_swap(db: Session, swap: schemas.SwapBase):
    db_swap = models.Swap(**swap.dict())
    db.add(db_swap)
    db.commit()
    db.refresh(db_swap)
    return db_swap

# ----- REVIEWS -----
def add_review(db: Session, review: schemas.ReviewBase, user_id: int):
    db_review = models.Review(**review.dict(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

