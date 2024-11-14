from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database, schemas, models, utils, oauth2

router = APIRouter(tags=["Authentication"])

@router.post('/login', response_model=schemas.Token)
def login(user_crendentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
  user = db.query(models.Users).filter(models.Users.email == user_crendentials.username).first()
  
  if not user:
    raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail="Invalid credentials")
  
  if not utils.verify(user_crendentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail="Invalid credentials")
  
  access_token = oauth2.create_access_token(data = {"user_id": user.id})
  
  return {"access_token": access_token, "token_type": "bearer"}
