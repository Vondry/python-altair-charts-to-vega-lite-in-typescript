"""Static chart spec endpoints."""
import json
from pathlib import Path
from fastapi import APIRouter, Query, HTTPException
from charts import create_time_series
from config import STATIC_SPECS_DIR

router = APIRouter(prefix="/api/data", tags=["static-charts"])


def load_static_spec(name: str) -> dict:
    """
    Load a pre-generated static Vega-Lite specification.
    
    Args:
        name: The name of the spec file (without .json extension)
        
    Returns:
        The loaded Vega-Lite specification as a dictionary
        
    Raises:
        HTTPException: If the spec file is not found
    """
    file_path = STATIC_SPECS_DIR / f"{name}.json"
    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Static spec '{name}' not found. Run build_static_specs.py to generate specs."
        )
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


@router.get("/sales-by-region")
async def sales_by_region():
    """Serve pre-built bar chart showing sales by region."""
    return load_static_spec("sales-by-region")


@router.get("/revenue-trend")
async def revenue_trend():
    """Serve pre-built line chart showing monthly revenue trend."""
    return load_static_spec("revenue-trend")


@router.get("/product-distribution")
async def product_distribution():
    """Serve pre-built pie chart showing product category distribution."""
    return load_static_spec("product-distribution")


@router.get("/price-volume-scatter")
async def price_volume_scatter():
    """Serve pre-built scatter plot showing price vs volume correlation."""
    return load_static_spec("price-volume-scatter")


@router.get("/time-series")
async def time_series(days: int = Query(default=30, ge=1, le=365, description="Number of days to display")):
    """
    Serve pre-built time series chart.
    
    Falls back to dynamic generation for non-standard day values.
    """
    if days == 30:
        return load_static_spec("time-series-30")
    elif days == 90:
        return load_static_spec("time-series-90")
    else:
        # Fallback to dynamic generation for other values
        return create_time_series(days)


@router.get("/multi-line")
async def multi_line():
    """Serve pre-built multi-line chart with interactive legend."""
    return load_static_spec("multi-line")


@router.get("/stacked-bar")
async def stacked_bar():
    """Serve pre-built stacked bar chart for composition analysis."""
    return load_static_spec("stacked-bar")


@router.get("/heatmap")
async def heatmap():
    """Serve pre-built heatmap showing activity patterns."""
    return load_static_spec("heatmap")


@router.get("/brush-selection")
async def brush_selection():
    """Serve pre-built brush selection chart for zooming."""
    return load_static_spec("brush-selection")


@router.get("/boxplot")
async def boxplot():
    """Serve pre-built box plot for distribution analysis."""
    return load_static_spec("boxplot")


@router.get("/histogram")
async def histogram():
    """Serve pre-built histogram for frequency distribution."""
    return load_static_spec("histogram")


@router.get("/area-chart")
async def area_chart():
    """Serve pre-built area chart for cumulative trends."""
    return load_static_spec("area-chart")


@router.get("/grouped-bar")
async def grouped_bar():
    """Serve pre-built grouped bar chart for comparison."""
    return load_static_spec("grouped-bar")


@router.get("/waterfall")
async def waterfall():
    """Serve pre-built waterfall chart for sequential changes."""
    return load_static_spec("waterfall")


@router.get("/treemap")
async def treemap():
    """Serve pre-built treemap for hierarchical data."""
    return load_static_spec("treemap")


@router.get("/radar")
async def radar():
    """Serve pre-built radar chart for multivariate comparison."""
    return load_static_spec("radar")


@router.get("/candlestick")
async def candlestick():
    """Serve pre-built candlestick chart for OHLC financial data."""
    return load_static_spec("candlestick")
