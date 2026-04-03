from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models # Hamari models.py file
from database import SessionLocal, engine # Hamari database.py file

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

@app.get("/stock/")
def get_stock(db : Session = Depends(get_db)):
    all_stocks = db.query(models.Stock).all()
    return {"data":all_stocks}
@app.post("/add-stock/")
def add_stock(name: str,price: int, db: Session = Depends(get_db)):
    new_data = models.Stock(name= name.upper(),price = price)
    db.add(new_data)
    db.commit()
    return {"status":"Success","saved_data":new_data}
@app.get("/search/{name}")
def search(name: str , db:Session = Depends(get_db)):
    stock = db.query(models.Stock).filter(models.Stock.name == name.upper()).first()
    if stock:
        return{"status":f"success we've found stock {stock.name}","price":stock.price} 
    else:
        return {"message":"not exist"}
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