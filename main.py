import uvicorn
from app.__init__ import app  

if __name__ == '__main__':
    uvicorn.run(
        "app.__init__:app", 
        reload=True,host="0.0.0.0",port=8000
    )

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


