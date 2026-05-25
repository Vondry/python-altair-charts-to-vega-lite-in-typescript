"""Application configuration and constants."""
from pathlib import Path

# Application metadata
APP_TITLE = "Chart Demo API"
APP_VERSION = "2.0.0"
TOTAL_CHARTS = 17

# Paths
BASE_DIR = Path(__file__).parent
STATIC_SPECS_DIR = BASE_DIR / "static_specs"

# CORS settings
CORS_ORIGINS = ["*"]
CORS_METHODS = ["GET"]
CORS_HEADERS = ["*"]

# API documentation
API_DESCRIPTION = """
Comprehensive chart visualization API with dual rendering modes:
- **Dynamic Mode**: Generates Vega-Lite specs on-demand using Altair
- **Static Mode**: Serves pre-built specs generated at build time
"""
