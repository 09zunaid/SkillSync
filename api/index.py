from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
import json
from pipeline import ProcessingPipeline

app = FastAPI()

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = ProcessingPipeline()

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...), 
    job_description: str = Form(...) # Expecting raw JD text
):
    try:
        content = await file.read()
        
        # Pass text directly to pipeline
        result = pipeline.process_application(content, job_description)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
