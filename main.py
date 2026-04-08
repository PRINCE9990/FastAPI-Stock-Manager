from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models # Hamari models.py file
from database import SessionLocal, engine # Hamari database.py file
import schemas
from typing import List
from fastapi import HTTPException

# 1. Database Table Create Karo (Ye line file bana degi)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. Dependency: Database se connection kholna aur kaam ke baad band karna
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stock/",response_model = List[schemas.StockResponse])
def get_stock(db : Session = Depends(get_db)):
    all_stocks = db.query(models.Stock).all()
    return all_stocks
@app.post("/add-stock/", response_model=schemas.StockResponse)
def add_stock(stock = schemas.StockCreate, db: Session = Depends(get_db)):
    new_stock = models.Stock(name= stock.name.upper(),price = stock.price)
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock
@app.get("/search/{name}", response_model = schemas.StockResponse)
def search(name: str , db:Session = Depends(get_db)):
    stock = db.query(models.Stock).filter(models.Stock.name == name.upper()).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found") 
    return stock
@app.delete("/delete/{name}")
def delete(name:str, db :Session = Depends(get_db)):
    stock = db.query(models.Stock).filter(models.Stock.name == name.upper()).first()
    if(stock):
        db.delete(stock)
        db.commit()
        return{"message":f"the stock {name.upper()} is deleted"}
    else:
        return{"meessage":"not found"}
@app.put("/update/{old_name}/{new_name}")
def update(old_name:str,new_name:str, db : Session= Depends(get_db)):
    data = db.query(models.Stock).filter(models.Stock.name == (old_name.upper())).first()
    if(data):
        data.name = new_name.upper()
        db.commit()
        return{"message":f"{old_name.upper()} is updated with {new_name.upper()}"}
    else:
        return{"message":"not found"}