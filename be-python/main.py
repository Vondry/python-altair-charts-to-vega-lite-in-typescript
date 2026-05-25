"""FastAPI application serving Vega-Lite chart specifications."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import (
    APP_TITLE,
    APP_VERSION,
    API_DESCRIPTION,
    TOTAL_CHARTS,
    CORS_ORIGINS,
    CORS_METHODS,
    CORS_HEADERS
)
from routes import charts_router, data_router, metadata_router

# Initialize FastAPI application
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=API_DESCRIPTION
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=CORS_METHODS,
    allow_headers=CORS_HEADERS,
)

# Register routers
app.include_router(metadata_router)
app.include_router(charts_router)
app.include_router(data_router)


@app.get("/", tags=["root"])
async def root():
    """
    API root endpoint providing service information.
    
    Returns overview of available endpoints and rendering modes.
    """
    return {
        "message": f"{APP_TITLE} - Comprehensive Visualization Library",
        "version": APP_VERSION,
        "total_charts": TOTAL_CHARTS,
        "modes": {
            "charts": "Dynamic: Backend generates Vega-Lite specs with Altair on-demand",
            "data": "Static: Pre-built Vega-Lite specs generated at build time"
        },
        "endpoints": {
            "metadata": ["/api/chart-sets/charts", "/api/chart-sets/data"],
            "dynamic_charts": "/api/charts/* (on-demand Altair generation)",
            "static_charts": "/api/data/* (pre-built specs)"
        },
        "docs": {
            "swagger": "/docs",
            "redoc": "/redoc"
        }
    }
