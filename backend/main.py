from fastapi import FastAPI
from database import init_db
from routers import auth, tenant, landlord, booking, favorite

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("🚀 Starting RentEase API...")
    init_db()
    print("✅ Database initialized successfully!")

app.include_router(auth.router)
app.include_router(tenant.router)
app.include_router(landlord.router)
app.include_router(booking.router)
app.include_router(favorite.router)

@app.get("/")
def root():
    return {"message": "RentEase API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
