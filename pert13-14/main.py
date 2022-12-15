from fastapi import FastAPI, HTTPException
from schemas.mahasiswa import Mahasiswa
from config.db import con
from models.index import mahasiswas
app=FastAPI()

# best way to make api
@app.get('/api/mahasiswas')
async def index():
    data=con.execute(mahasiswas.select()).fetchall()
    return {
        "success": True,
        "data":data
    }

# insert data
@app.post('/api/mahasiswas')
async def store(mahasiswa:Mahasiswa):
    data=con.execute(mahasiswas.insert().values(
        name=mahasiswa.name,
        email=mahasiswa.email,
        nim=mahasiswa.nim,
        jurusan=mahasiswa.jurusan,
    ))

    if data.is_insert:
        return {
            "success": True,
            "msg":"Berhasil Insert Data"
        }
    else:
         return {
            "success": False,
            "msg":"Error"
        }

# edit data
@app.patch('/api/mahasiswas/{id}')
async def edit_data(id:int):
    data=con.execute(mahasiswas.select().where(mahasiswas.c.id==id)).fetchall()
    return {
        "success": True,
        "data":data
    }

# update data

@app.put('/api/mahasiswas/{id}')
async def update(id:int,mahasiswa:Mahasiswa):
    data=con.execute(mahasiswas.update().values(
        name=mahasiswa.name,
        email=mahasiswa.email,
        nim=mahasiswa.nim,
        jurusan=mahasiswa.jurusan,
    ).where(mahasiswas.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"Berhasil Update Data"
        }
    else:
         return {
            "success": False,
            "msg":"Error"
        }

# delete data
@app.delete('/api/mahasiswas/{id}')
async def delete(id:int):
    data=con.execute(mahasiswas.delete().where(mahasiswas.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"Berhasil Hapus Data!"
        }
    else:
         return {
            "success": False,
            "msg":"Error"
        }

# search data

@app.get('/api/mahasiswas/{search}')
async def search(search):
    data=con.execute(mahasiswas.select().where(mahasiswas.c.name.like('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data":data
    }