from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from models import Base
from crud import get_credits, add_credits, deduct_credits, reset_credits, set_schema_from_sql

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. GET credits
@app.get("/api/credits/{user_id}")
def read_credits(user_id: int, db: Session = Depends(get_db)):
    credits = get_credits(db, user_id)
    if credits:
        return {"user_id": user_id, "credits": credits.credits, "last_updated": credits.last_updated}
    raise HTTPException(status_code=404, detail="User not found")

# 2. POST credits/add
@app.post("/api/credits/{user_id}/add")
def add_credits_api(user_id: int, payload: dict = Body(...), db: Session = Depends(get_db)):
    amount = payload.get("amount")
    credits = add_credits(db, user_id, amount)
    return {"user_id": user_id, "credits": credits.credits, "last_updated": credits.last_updated}

# 3. POST credits/deduct
@app.post("/api/credits/{user_id}/deduct")
def deduct_credits_api(user_id: int, payload: dict = Body(...), db: Session = Depends(get_db)):
    amount = payload.get("amount")
    credits = deduct_credits(db, user_id, amount)
    return {"user_id": user_id, "credits": credits.credits, "last_updated": credits.last_updated}

# 4. PATCH credits/reset
@app.patch("/api/credits/{user_id}/reset")
def reset_credits_api(user_id: int, db: Session = Depends(get_db)):
    credits = reset_credits(db, user_id)
    return {"user_id": user_id, "credits": credits.credits, "last_updated": credits.last_updated}

# 5. API for external schema update
@app.post("/api/schema/update")
def update_schema(payload: dict = Body(...), db: Session = Depends(get_db)):
    sql = payload.get("sql")
    set_schema_from_sql(db, sql)
    return {"detail": "Schema updated"}
