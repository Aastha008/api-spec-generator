from src.core import CodeParser
import os

def test_parser():
    parser = CodeParser()
    endpoints = parser.extract_endpoints(os.getcwd())
    assert isinstance(endpoints, list)