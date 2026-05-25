"""Metadata endpoints for chart sets."""
from fastapi import APIRouter
from chart_sets import STATIC_CHART_SET, DYNAMIC_CHART_SET

router = APIRouter(prefix="/api/chart-sets", tags=["metadata"])


@router.get("/charts")
async def get_charts_set():
    """
    Get metadata for dynamic chart endpoints.
    
    Returns list of all chart endpoints that generate Vega-Lite specs
    on-demand using Altair.
    """
    return STATIC_CHART_SET


@router.get("/data")
async def get_data_set():
    """
    Get metadata for static chart endpoints.
    
    Returns list of all data endpoints that serve pre-built Vega-Lite
    specs generated at build time.
    """
    return DYNAMIC_CHART_SET
