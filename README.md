# FastAPI Stock Manager 📈
Ye mera pehla Python Backend project hai.
- Add, Delete, Search, aur Update Stocks.

### 🚀 New: Database Integration
Added SQLAlchemy for ORM.
Connected SQLite database for persistent storage.
CRUD operations (Create, Read, Update, Delete) are now database-backed.

### 🛠️ Technical Stack
* **Framework:** FastAPI
* **Database:** SQLite (Persistent Storage)
* **ORM:** SQLAlchemy
* **Validation:** Pydantic (Schemas)

### 📂 Project Structure
* `main.py` - API Routes aur Logic
* `models.py` - Database Tables ka structure
* `schemas.py` - Pydantic Models (Data Validation)
* `database.py` - Database Connection setup

### 🚀 How to Run
1. Install requirements:
   `pip install fastapi uvicorn sqlalchemy`
2. Run the server:
   `python -m uvicorn main:app --reload`
3. Access Documentation:
   Go to `http://127.0.0.1:8000/docs` to test CRUD operations.