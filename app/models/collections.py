import sqlalchemy as sa

from app.models import Base


class Collections(Base):
    __tablename__ = 'collections'
    id = sa.Column('id', sa.Integer, primary_key=True)
    nama = sa.Column('nama_barang', sa.String)
    kategori = sa.Column('kategori_barang', sa.String)
    harga = sa.Column('harga_barang', sa.String)
    durasi = sa.Column('durasi_barang', sa.Integer)
    diskon = sa.Column('diskon_barang', sa.Integer)
    jarak = sa.Column('jarak_barang', sa.Integer)