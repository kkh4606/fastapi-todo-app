from passlib.context import CryptContext



pwd_context = CryptContext(schemes=['bcrypt'])


# hash password

def hash_password(password):
    return pwd_context.hash(password)


# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)