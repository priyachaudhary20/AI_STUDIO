from fastapi import FastAPI
from workflows.orchestrator import run_pipeline

app = FastAPI()


@app.post("/generate-film")
def generate():

    video = run_pipeline()

    return {"video": video}