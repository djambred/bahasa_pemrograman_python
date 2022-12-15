from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


mahasiswas=Table(
    'Mahasiswas',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('nim',String(255)),
    Column('jurusan',String(255)),
)