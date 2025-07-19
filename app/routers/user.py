from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, utils, oauth2
from sqlalchemy.orm import Session
from typing import List



router = APIRouter(prefix='/users', tags=['User'])



@router.get('/', response_model=List[schemas.UserOut])
def get_users(db:Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    users = db.query(models.User).all()
    return users

@router.post('/create', response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)

def create_user(user:schemas.UserCreate, db : Session= Depends(database.get_db)):

    hashed_password = utils.hash_password(user.password)

    new_user = models.User(email=user.email , password = hashed_password)

    

   

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
