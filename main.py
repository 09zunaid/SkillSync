from api.index import app
from fastapi.middleware.cors import CORSMiddleware

# Allow specific Vercel origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://skillsync-ui.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
