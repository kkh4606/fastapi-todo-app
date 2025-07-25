from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2


router = APIRouter(prefix="/todos", tags=["TODOS"])


@router.get("/")
def get_todos(db: Session = Depends(database.get_db), current_user : models.User = Depends(oauth2.get_current_user)):
    todos = db.query(models.Todo).filter(models.Todo.owner_id == current_user.id).all()
    return todos


@router.get("/{id}")
def get_todo(id: int, db: Session = Depends(database.get_db), current_user:models.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == id, models.Todo.owner_id == current_user.id).first()
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )

    return todo


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.TodoOut)
def add_todo(todo_data: schemas.AddTodo, db: Session = Depends(database.get_db),
             current_user : models.User = Depends(oauth2.get_current_user)):
    

   
    
    
    new_todo = models.Todo(**todo_data.model_dump(), owner_id = current_user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.put("/{id}")
def update_todo(
    id: int, update_todo: schemas.AddTodo, db: Session = Depends(database.get_db),
    current_user : models.User = Depends(oauth2.get_current_user)
):
    todo_query = db.query(models.Todo).filter(models.Todo.id == id, models.Todo.owner_id == current_user.id)
    todo = todo_query.first()
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="todo not found"
        )

    todo_data = update_todo.dict(exclude_unset=True)

    for key, value in todo_data.items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, db: Session = Depends(database.get_db), current_user:models.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == id, models.Todo.owner_id == current_user.id).first()
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="todo not found"
        )
    db.delete(todo)
    db.commit()
    return
