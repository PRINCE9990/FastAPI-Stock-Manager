from fastapi import FastAPI
app = FastAPI()
my_stock =["YES","TATA","SBI"]
@app.get("/stock")
def get_all_stock():
    return{"stock":my_stock}
@app.get("/add/{name}")
def add(name:str):
    my_stock.append(name.upper())
    return{"message":f"stock {name.upper()} is successfully added in the list","stockss":my_stock}
@app.get("/search/{name}")
def search(name: str):
    if(name.upper() in my_stock):
        return{"message": f"we've got {name.upper()}"}
    else:
        return {"message":"not exist"}
@app.get("/delete/{name}")
def delete(name:str):
    names = name.upper()
    if(names in my_stock):
        my_stock.remove(names)
        return{"message":f"{names} is deleted"}
    else:
        return{"message":"not found"}
@app.get("/update/{old_name}/{new_name}")
def update(old_name:str,new_name:str):
    names = old_name.upper()
    if(names in my_stock):
        index = my_stock.index(names)
        my_stock[index] = new_name.upper()
        return{"message":f"{names} is updated with {new_name.upper()}"}
    else:
        return{"message":"not found"}