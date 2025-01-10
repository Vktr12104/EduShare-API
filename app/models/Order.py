import sqlalchemy as sa

from app.models import Base


class Order(Base):
    __tablename__ = 'orders'
    id = sa.Column('id', sa.Integer, primary_key=True)
    user_id = sa.Column('user_id', sa.Integer)
    nama = sa.Column('nama_barang', sa.String)
    kuantitas = sa.Column('kuantitas_pesan', sa.Integer)