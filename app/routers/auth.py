from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, models, utils, oauth2, schemas





router = APIRouter(prefix='/user-login', tags=['Authtentication'])




@router.post('/')
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()



    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentials')
    
    if not utils.verify_password(user_credentials.password , user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentials')
    
    # crete token if login success

    access_token = oauth2.create_access_token(data={"sub" : str(user.id)})
    return {'access_token' :access_token, 'token_type' : 'bearer' }
    
