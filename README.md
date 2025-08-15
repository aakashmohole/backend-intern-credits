
# Credit Management API

This project is a Credit Management service built with FastAPI and PostgreSQL (NeonDB). It tracks user credits for actions such as publishing articles, commenting, and mentoring. The service exposes APIs to query and modify user credits, supports dynamic schema updates, and runs a daily background job to add credits automatically.

---

## Features

- PostgreSQL schema with `users` and `credits` tables.
- REST API endpoints to:
  - Get user credit balance and last updated timestamp.
  - Add credits.
  - Deduct credits (without going negative).
  - Reset credits to zero.
  - Dynamically update the database schema with raw SQL.
- Background job to add 5 credits daily to all users at midnight UTC.
- Postman collection for easy testing.

---

## Technology Stack

- FastAPI (Python) for the API server.
- SQLAlchemy for ORM.
- PostgreSQL via NeonDB.
- APScheduler for background scheduling.
- Python-dotenv for environment configuration.

---

## Setup Instructions

### 1. Clone the repository

```
git clone 
cd backend-intern-credits/src
```

### 2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside `src/` directory with:

```
DATABASE_URL=postgresql+psycopg://:@/
```

Replace placeholders with your NeonDB or PostgreSQL connection details.

### 5. Initialize the database schema

Run the SQL commands in `schema.sql` on your database. For example:

```
psql -h  -U  -d  -f ../schema.sql
```

### 6. Run the API server

```
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`.

Swagger UI docs: `http://localhost:8000/docs`

---

## API Endpoints

| HTTP Method | Endpoint                  | Description                              |
|-------------|---------------------------|------------------------------------------|
| GET         | /api/credits/{user_id}    | Get current credit balance and timestamp|
| POST        | /api/credits/{user_id}/add| Add credits to the user                  |
| POST        | /api/credits/{user_id}/deduct | Deduct credits (balance cannot go negative) |
| PATCH       | /api/credits/{user_id}/reset | Reset user’s credits to zero              |
| POST        | /api/schema/update         | Dynamically update database schema via SQL |

---

## Background Job

- Adds 5 credits to every user daily at midnight UTC.
- Runs automatically with the API server using APScheduler.

---

## Testing

- Use the included Postman collection `postman_collection.json` to test endpoints.
- Import the collection in Postman and modify parameters as needed.

---

## Notes

- Ensure users exist in the `users` table before adding credits.
- The schema update endpoint accepts raw SQL—use with caution.
- Use environment variables for sensitive data like database credentials.

---
