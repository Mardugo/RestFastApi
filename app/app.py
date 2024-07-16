from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from modelo.schemas import ItemCreateOrUpdate, Item, SuccessMessage
from controlador import crud
from modelo.database import SessionLocal


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=ItemCreateOrUpdate)
def create_item(item: ItemCreateOrUpdate, db: Session = Depends(get_db)):
    return crud.create_item(db=db,item=item)

@app.get("/items/", response_model=list[Item])
def read_items(limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item: ItemCreateOrUpdate, item_id: int, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item=item, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_item

@app.delete("/items/{item_id}", response_model=SuccessMessage)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
