from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    password: str

class BukuBase(BaseModel):
    judul: str
    katagori: str
    pengarang: str
    penerbit: str
    rak: str
    isbn: int
    jumlah: int

class Pinjam(BaseModel):
    notel: int
    kelas: str
    nama: str
    judul: str
    tanggal_pinjam: str
    tanggal_kembali: str
    jumlah: int
    status: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/{username}", status_code=status.HTTP_200_OK)
async def read_user(username: str, db: db_dependency):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')
    return user 

@app.post("/buku/", status_code=status.HTTP_201_CREATED)
async def create_buku(buku: BukuBase, db: db_dependency):
    db_buku = models.Buku(**buku.dict())
    db.add(db_buku)
    db.commit()

@app.get("/buku/{judul}", status_code=status.HTTP_200_OK)
async def read_user(judul: str, db: db_dependency):
    buku = db.query(models.Buku).filter(models.Buku.judul == judul).first()
    if buku is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Buku Not Found')
    return buku 