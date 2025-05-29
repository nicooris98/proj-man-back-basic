from fastapi import FastAPI
from app.db.init_db import init_db
from contextlib import asynccontextmanager
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware

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
    allow_origins=["*"],  # En producción, reemplazar "*" con dominio frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],
)