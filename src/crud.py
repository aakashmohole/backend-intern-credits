from sqlalchemy.orm import Session
from models import Credits

def get_credits(db: Session, user_id: int):
    return db.query(Credits).filter(Credits.user_id == user_id).first()

def add_credits(db: Session, user_id: int, amount: int):
    credits = get_credits(db, user_id)
    if credits:
        credits.credits += amount
        credits.last_updated = func.now()
        db.commit()
        db.refresh(credits)
    return credits

def deduct_credits(db: Session, user_id: int, amount: int):
    credits = get_credits(db, user_id)
    if credits and credits.credits >= amount:
        credits.credits -= amount
        credits.last_updated = func.now()
        db.commit()
        db.refresh(credits)
    return credits

def reset_credits(db: Session, user_id: int):
    credits = get_credits(db, user_id)
    if credits:
        credits.credits = 0
        credits.last_updated = func.now()
        db.commit()
        db.refresh(credits)
    return credits

def set_schema_from_sql(db, sql: str):
    db.execute(sql)
    db.commit()
