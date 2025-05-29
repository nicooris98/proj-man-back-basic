from fastapi import FastAPI
from app.db.init_db import init_db
from contextlib import asynccontextmanager
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

FRONT_URL = os.getenv('FRONT_URL')

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Arrancando app...")
    init_db()  # Esto crea las tablas
    yield  # Aquí FastAPI ejecuta el servidor
    print("Apagando app...")

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000)) 
    uvicorn.run(app, host="0.0.0.0", port=port)