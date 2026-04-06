from fastapi import FastAPI
from database import init_db
from routers import auth, tenant, landlord, booking, favorite

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("🚀 Starting RentEase API...")
    init_db()
    print("✅ Database initialized successfully!")

app.include_router(auth.router, prefix="/api")
app.include_router(tenant.router, prefix="/api")
app.include_router(landlord.router, prefix="/api")
app.include_router(booking.router, prefix="/api")
app.include_router(favorite.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "RentEase API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
