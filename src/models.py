from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class EndpointMetadata(BaseModel):
    path: str
    method: str
    parameters: List[Dict[str, Any]] = []
    description: Optional[str] = None

class OpenAPISpec(BaseModel):
    openapi: str = "3.0.0"
    info: Dict[str, str] = {"title": "Generated API", "version": "1.0.0"}
    paths: Dict[str, Any] = {}

class GenerationJob(BaseModel):
    job_id: str
    status: str = "pending"
    result: Optional[OpenAPISpec] = None