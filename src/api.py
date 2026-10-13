from fastapi import FastAPI
from .models import GenerationJob, OpenAPISpec
from .core import CodeParser, SpecGenerator

app = FastAPI()
jobs: dict[str, GenerationJob] = {}

@app.post("/generate")
async def start_generation(repo_path: str):
    parser = CodeParser()
    generator = SpecGenerator()
    endpoints = parser.extract_endpoints(repo_path)
    spec = generator.generate_spec(endpoints)
    job = GenerationJob(job_id="1", status="completed", result=spec)
    jobs[job.job_id] = job
    return job