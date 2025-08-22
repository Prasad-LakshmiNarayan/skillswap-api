from fastapi import FastAPI
from routers import users, skills, swaps, reviews, messages
import models
from database import engine
import auth   # 👈 NEW: import auth router

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SkillSwap API", version="1.0")

# 👇 Register all routers
app.include_router(auth.router)      # 👈 Adds signup/login
app.include_router(users.router)
app.include_router(skills.router)
app.include_router(swaps.router)
app.include_router(reviews.router)
app.include_router(messages.router)

@app.get("/")
def root():
    return {"message": "Welcome to SkillSwap 🚀"}
