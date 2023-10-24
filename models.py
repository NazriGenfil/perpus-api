from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(String(50))

class Buku(Base):
    __tablename__ = 'buku'

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String(50))
    katagori = Column(String(50))
    pengarang = Column(String(50))
    penerbit = Column(String(50))
    rak = Column(String(50))
    isbn = Column(Integer, unique=True)
    jumlah = Column(Integer)

class Pinjam(Base):
    __tablename__ = 'pinjaman'

    id = Column(Integer, primary_key=True, index=True)
    notel = Column(Integer)
    kelas = Column(String(50))
    nama = Column(String(50))
    judul = Column(String(50))
    tanggal_pinjam = Column(String(50))
    tanggal_kembali = Column(String(50))
    jumlah = Column(Integer)
    status = Column(Boolean)
