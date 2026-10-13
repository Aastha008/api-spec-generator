import uvicorn
import typer
from src.api import app as api_app
from src.cli import app as cli_app

if __name__ == "__main__":
    # Simple logic to switch between CLI and API mode
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        uvicorn.run(api_app, host="0.0.0.0", port=8000)
    else:
        cli_app()