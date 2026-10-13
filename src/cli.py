import typer
from .core import CodeParser, SpecGenerator

app = typer.Typer()

@app.command()
def scan(path: str):
    parser = CodeParser()
    endpoints = parser.extract_endpoints(path)
    typer.echo(f"Found {len(endpoints)} endpoints.")

if __name__ == "__main__":
    app()