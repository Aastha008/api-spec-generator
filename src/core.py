import ast
import os
from typing import List
from openai import OpenAI
from .models import EndpointMetadata, OpenAPISpec

class CodeParser:
    def extract_endpoints(self, directory: str) -> List[EndpointMetadata]:
        endpoints = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    with open(os.path.join(root, file), "r") as f:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                for decorator in node.decorator_list:
                                    if isinstance(decorator, ast.Call) and hasattr(decorator.func, 'attr'):
                                        endpoints.append(EndpointMetadata(path="/", method=decorator.func.attr.upper()))
        return endpoints

class SpecGenerator:
    def __init__(self):
        self.client = OpenAI()

    def generate_spec(self, endpoints: List[EndpointMetadata]) -> OpenAPISpec:
        # Simplified logic for demonstration
        paths = {e.path: {e.method.lower(): {"summary": e.description or "Auto-generated"}} for e in endpoints}
        return OpenAPISpec(paths=paths)