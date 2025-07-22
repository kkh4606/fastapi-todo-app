from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from . import database, models, schemas

from app.config import settings


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_sheme = OAuth2PasswordBearer(tokenUrl='login')


# create jwt

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# verify jwt

def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id : str = payload.get('sub')

        if user_id is None:
            raise credentials_exception
        return  schemas.TokenData(id = str(user_id))
    
    
    except JWTError:
        raise credentials_exception
    
    

# get current user

def get_current_user(token:str = Depends(oauth2_sheme), db:Session = Depends(database.get_db)):
    
    credentials_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentaials', headers={"WWW-Authtenticate" : 'Bearer'})

    token = verify_access_token(token, credentials_exceptions)

    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user






