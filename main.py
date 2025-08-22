from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="SkillSwap API")

# Temporary "database" (in-memory for now, later we connect to real DB)
users_db = {}
skills_db = {}
user_counter = 1
skill_counter = 1

# Pydantic models
class User(BaseModel):
    name: str
    email: str

class Skill(BaseModel):
    user_id: int
    skill_name: str
    description: Optional[str] = None

# ---------------------------
# User Routes
# ---------------------------

@app.post("/users")
def create_user(user: User):
    global user_counter
    users_db[user_counter] = {"id": user_counter, **user.dict()}
    user_counter += 1
    return users_db[user_counter - 1]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.get("/users")
def list_users():
    return list(users_db.values())

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id].update(user.dict())
    return users_db[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    deleted = users_db.pop(user_id)
    return {"message": "User deleted", "user": deleted}

# ---------------------------
# Skill Routes
# ---------------------------

@app.post("/skills")
def create_skill(skill: Skill):
    global skill_counter
    if skill.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    skills_db[skill_counter] = {"id": skill_counter, **skill.dict()}
    skill_counter += 1
    return skills_db[skill_counter - 1]

@app.get("/skills")
def list_skills():
    return list(skills_db.values())

@app.get("/skills/{skill_id}")
def get_skill(skill_id: int):
    if skill_id not in skills_db:
        raise HTTPException(status_code=404, detail="Skill not found")
    @app.get("/")
    def root():
        return {"message": "Welcome to SkillSwap API! 🚀 Use /docs to explore the API."}
    

    return skills_db[skill_id]
