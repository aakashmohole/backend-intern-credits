from apscheduler.schedulers.background import BackgroundScheduler
from db import SessionLocal
from models import Credits
from sqlalchemy.sql import func

def add_daily_credits():
    db = SessionLocal()
    try:
        creds = db.query(Credits).all()
        for cred in creds:
            cred.credits += 5
            cred.last_updated = func.now()
        db.commit()
    finally:
        db.close()

scheduler = BackgroundScheduler(timezone='UTC')
scheduler.add_job(add_daily_credits, 'cron', hour=0, minute=0)
scheduler.start()
