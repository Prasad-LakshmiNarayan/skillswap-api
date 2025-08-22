from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Turn a plain password into a hashed one."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if the password is correct."""
    return pwd_context.verify(plain_password, hashed_password)

# ----- JWT Setup -----
SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_ME"   # ⚠️ use env var in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Make a JWT token with an expiry time."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
