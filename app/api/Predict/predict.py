from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

model = pickle.load(open("models.pkl", "rb"))
kategori_encoder = LabelEncoder()
kategori_encoder.fit(['Seragam', 'Kesehatan', 'Mainan Anak', 'Hobi', 'Buku'])
pembayaran_encoder = LabelEncoder()
pembayaran_encoder.fit(['Bayar_Langsung', 'Cicilan_Tanpa_Kartu', 'Barter', 'Kredit_Bank', 'Pinjam'])

feature_names = ['Kategori_Barang', 'Harga_Barang', 'Diskon (%)', 'Jumlah_Pembelian', 'Durasi_Kepemilikan (bulan)', 'Jarak (km)']

class PredictionRequest(BaseModel):
    Kategori_Barang: str
    Harga_Barang: float
    Diskon: float
    Jumlah_Pembelian: float
    Durasi_Kepemilikan: float
    Jarak: float
async def predict(request_data: PredictionRequest):
    try:
        kategori_barang_encoded = kategori_encoder.transform([request_data.Kategori_Barang])[0]
        numeric_features = [
            request_data.Harga_Barang,
            request_data.Diskon,
            request_data.Jumlah_Pembelian,
            request_data.Durasi_Kepemilikan,
            request_data.Jarak
        ]
        features = [kategori_barang_encoded] + numeric_features
        features_df = pd.DataFrame([features], columns=feature_names)
        prediction = model.predict(features_df)
        predicted_label = pembayaran_encoder.inverse_transform(prediction)

        return JSONResponse({"prediction": f"Saran Metode Pembayaran : {predicted_label[0]}"})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

async def predict_dev(request_data: PredictionRequest):
    try:
        kategori_barang_encoded = kategori_encoder.transform([request_data.Kategori_Barang])[0]
        numeric_features = [
            request_data.Harga_Barang,
            request_data.Diskon,
            request_data.Jumlah_Pembelian,
            request_data.Durasi_Kepemilikan,
            request_data.Jarak
        ]
        features = [kategori_barang_encoded] + numeric_features
        features_df = pd.DataFrame([features], columns=feature_names)
        prediction = model.predict(features_df)
        predicted_label = pembayaran_encoder.inverse_transform(prediction)

        return JSONResponse({"prediction": f"Saran Metode Pembayaran : {predicted_label[0]}"}), 200
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
