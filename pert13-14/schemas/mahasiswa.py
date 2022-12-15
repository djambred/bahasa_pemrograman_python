from pydantic import BaseModel

class Mahasiswa(BaseModel):
    name:str
    email:str
    nim:int
    jurusan:str