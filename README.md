Dibuat oleh Viktor Arsindiantoro Siringoringo - 18222083
Dibuat menggunakan Azure Container Instance, Anda dapat mengakses layanan melalui titik akhir berikut:
- Front End
	```
	https://edushare-fe.vercel.app/
	```
- Back end
  	```
	https://edushare.codebloop.my.id
	```
-  API Eksternal (FE):
  	```
	https://furina-encryption-service.codebloop.my.id/
	```
  - API Eksternal Dokumentasi:
  	```
	https://furina-encryption-service.codebloop.my.id/docs
	```

# Requirements
1. Docker
2. Python
3. SQLModel

# How to run locally (using Docker Compose)
1. Make sure that Docker daemon already running
2. Make a virtual environment with this command
```
python -m venv venv
```
4. Activate virtual environment with this command
- Windows
	```
	source venv/Scripts/activate
	```
- Linux & Mac  :
  	```
	source venv/bin/activate
	```
5. Use this command below to run the app
  	```
	docker compose -p my_project up --build --remove-orphans -d
	```

# Dokumentasi API EduShare
Selamat datang di API EduShare! API ini memungkinkan Anda untuk berinteraksi dengan platform BerbagiPendidikan, yang mencakup Autentikasi, Endpoint publik, dan akses aman ke data spesifik pengguna.

# URL Dasar Dokumentasi
URL dasar untuk API yang sudah dideploy adalah: 
```
https://edushare.codebloop.my.id
```
Anda dapat mengakses dokumentasi API interaktif menggunakan Swagger UI di:
```
https://edushare.codebloop.my.id/docs
https://edushare.codebloop.my.id/redoc
```
# Authentication
API EduShare menggunakan OAuth2 Bearer Tokens untuk mengamankan endpoint. Berikut adalah ringkasan mekanisme autentikasi:
## OAuth2 Bearer Tokens
- Dapatkan token melalui endpoint /api/v1/auth/login.
- Sertakan token dalam header Authorization:
```
Authorization: Bearer <token>
```
# Endpoint
## 1. Endpoint Autentikasi 
Endpoint untuk login dan registrasi serta profile pengguna
### POST /api/v1/auth/Register
- Deskripsi: Melakukan akses registrasi pengguna baru
- Body :
```
{
  "username": "string",
  "full_name": "string",
  "password": "string",
  "confirm_password": "string"
}
```
- Responses :
```
{
	"string"
}
```
### POST /api/v1/auth/Login
- Deskripsi: Melakukan Akses login dan penyediaan akses token dan refresh token
- Body :
```
{
  "username": "string",
  "password": "string"
}
```
- Responses Body :
```
{
  "data": {
    "user_id": 1,
    "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsInVzZXJuYW1lIjoic3RyaW5nIiwiaWF0IjoxNzMzOTMxODA3fQ.OjBcnZRZm38Wx8rX0vdcJBJYcVAU11UOTKqmKPnphIIV-wBn74C1DaKcHrZVmT6eJxdZ_JuWQJI89plmostGxW7bhrQvXAkrlVVq2Uq4RioIrI3vKxY_2icwsPXAqoxfAzZmKMh4l67ZTR6qlHN-WWthWWBT8R5qTN9IohL0CBK7GcV4h4bkGszZkb5jsY5sJz31OnBeUw0jznfWpH9wN28mPtlQcQw3r6dahZOpqWxBis3Y9Ye5ph_MIMOuE9R9iEVG_P1nKwXzXvsKBMFp4JCbzwJjsQezHhR0WbtrU-tkxhk5eWayVgOHdx0YfCf1t-w82TGH4GdH6Ca3HBOyPg",
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsInVzZXJuYW1lIjoic3RyaW5nIiwiaWF0IjoxNzMzOTMxODA3LCJleHAiOjE3MzM5MzIxMDd9.OenlCUjhpTr7PbNquw0udF_gAuTsZuDdat_4CPgFbFa2J016dcOvmx7nmuINmHzihKn_2cskCELVxhjyikNX0xb5y76dYIz7nESHCAXuJ9C0OYTqn6uOsKGOV3ZKzwZp4zi-d0XSDMXNv5DTMvBBbe_MQ_b5jZkepzosydVv0dKg7p5eRg4ogXkYKFUuky6Qz_YLf-G8zC031urmCAWW4Bsd0bBfbmev2Z3Dyibni-SUA1qDQydT6qJOCvffCpOOAI4FKYzvfcaSi4H7i-kz6d6ph_H5NDyqUmKGccwYMzS3o1wC8xnlNXXpBTYtuHOvKtaAVfiWXyz1rrmEM-pJdQ",
    "expired_at": 1733932107
  },
  "meta": {},
  "success": true,
  "code": 200,
  "message": "Success"
}
```
- Responses Header
```
 content-length: 1045 
 content-type: application/json 
 date: Wed,11 Dec 2024 15:43:26 GMT 
 server: uvicorn 
```
### POST /api/v1/auth/logout
- Deskripsi: Melakukan Akses logout dari akun
- Body :
```
{
  "refresh_token": "string"
}
```
- Responses Header
```
 date: Wed,11 Dec 2024 17:19:50 GMT 
 server: uvicorn 
```
### POST /api/v1/auth/refresh-token
- Deskripsi: Memberikan pembaharuan token
- Body :
```
{
  "refresh_token": "string"
}
```
- Responses Body : 
```
{
  "data": {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsInVzZXJuYW1lIjoic3RyaW5nIiwiZXhwIjoxNzMzOTMxMzE1LCJpYXQiOjE3MzM5MzEwMTV9.QXgANlDpH4cveDO4GMYtP25ntZt26eYv4Geyv2fR7Gni-llxLZPCaZfVYvyEQc1-gsKs-b50O7ZtNR8mVrZ7iP76pyNOploKOI1yJMqtd6SE5JUmUv_TydFzJ9EIfC01weTYZRezOT-I26dTJxYzBK6luQb1exAks3iPANVWzAeP3stZD4eGs3p76M0_-ly6jZJhkbx6KBfI6czgMhNHL8tuSP0hAxuaJnfHTF14OpuZewfxAghOk8rKEkaDSmYSDOeSK8m9dY6TQKlnInIthge3Pf9scila8-jBhyRaOMYx86VAxNFvC_Lbm2yw0oWQ8-29lGIsllLNMEaIXmVH9g",
    "expired_at": 1733931315
  },
  "meta": {},
  "success": true,
  "code": 200,
  "message": "Success"
}
```
### GET /api/v1/auth/profile
- Deskripsi: Mengambil data profile dengan metode authorization
- authorization :
```
Bearer Token
```
- Responses Body : 
```
{
  "code": 200,
  "data": {
    "full_name": "Shin Hayata",
    "id": 1000,
    "username": "shinhayata"
  },
  "message": "Success",
  "meta": {},
  "success": true
}
```
### PUT /api/v1/auth/profile
- Deskripsi: Melakukan update pada data profile dengan metode authorization
- authorization :
```
{
  "username": "string",
  "full_name": "string",
  "password": "string",
  "confirm_password": "string"
}
```
- Responses Header : 
```
 date: Wed,11 Dec 2024 15:44:21 GMT 
 server: uvicorn 
```
### POST /api/v1/auth/request_api_key
- Deskripsi: Melakukan Akses logout dari akun
- Body :
```
{
  "username": "string"
}
```
- Responses Header
```
{
  "api_key": "8c62ade9-8d96-4be2-8515-13ef66524961"
}
```
### GET /api/v1/auth/collect
- Deskripsi: Mendapatkan data collection produk
- Responses Header
```
[
  {
    "durasi": 50,
    "jarak": 2,
    "nama": "Buku Matematika",
    "kategori": "Buku",
    "harga": "50000",
    "id": 1,
    "diskon": 10
  }
]
```
### GET /api/v1/auth/collect/{collect_id}
- Deskripsi: Mendapatkan data detailed  dari suatu produk
- Parameters
```
collect_id:
```
- Responses Header
```
{
  "durasi": 99,
  "jarak": 2,
  "nama": "Seragam Sekolah",
  "kategori": "Seragam",
  "harga": "100000",
  "id": 2,
  "diskon": 15
}
```
### POST /api/v1/auth/order
- Deskripsi: Melakukan proses ordering
- authorization :Access_token
- Body :
```
{
  "nama": "string",
  "kuantitas": 0
}
```
- Responses Header
```
{
  "nama": "Buku",
  "id": 2,
  "kuantitas": 2,
  "user_id": 1
}
```
### POST /api/v1/auth/order/predict
- Deskripsi: Melakukan proses predict transaksi method
- Body :
```
{
  "Kategori_Barang": "string",
  "Harga_Barang": 0,
  "Diskon": 0,
  "Jumlah_Pembelian": 0,
  "Durasi_Kepemilikan": 0,
  "Jarak": 0
}
```
- Responses Body
```
{
  "prediction": "Saran Metode Pembayaran : Bayar_Langsung"
}
```
### POST /api/v1/auth/encrypt (API Eksternal)
- Deskripsi: Mengakses API Eksternal yang bertujuan untuk dapat mengirin pesan transaksi dan pembeli ke penjual
- Body :
```
{
  "text": "string",
  "sensitivity": "string"
}
```
- Responses Body
```
{
  "key_id": "L6BCNZUZ62cC0EPIfX0v5w",
  "cipher_text": "CgoYJQwv",
  "iv": "9byXAsKg0ljYh/f+2S2EVg=="
}
```
### POST /api/v1/auth/order/predict
- Deskripsi: Menerima predict api apabila ingin dipakai developer lain
- authorization :API_Key
- Body :
```
{
  "Kategori_Barang": "string",
  "Harga_Barang": 0,
  "Diskon": 0,
  "Jumlah_Pembelian": 0,
  "Durasi_Kepemilikan": 0,
  "Jarak": 0
}
```
- Responses Body
```
{
  "prediction": "Saran Metode Pembayaran : Bayar_Langsung"
}
```

# Contoh Akses 
## 1. Mendapatkan Access Token
- Metode: POST
- URL: ``` https://edu-share-api.vercel.app/api/v1/auth/login ```
username : String1
password : string
- Responses Header : 
```
{
  "code": 200,
  "data": {
    "acces_token": "jkl.mno.pqr",
    "expired_at": 123456,
    "refresh_token": "abc.def.ghi",
    "user_id": 1000
  },
  "message": "Success",
  "meta": {},
  "success": true
}
```
## 2. Mengambil Data dari profile
- Metode: GET
- URL: ``` https://edu-share-api.vercel.app/api/v1/auth/profile ```
```
Bearer Token
```
- Responses : 
```
{
  "data": {
    "id": 1,
    "username": "string",
    "full_name": "string"
  },
  "meta": {},
  "success": true,
  "code": 200,
  "message": "Success"
}
```
