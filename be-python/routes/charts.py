"""Dynamic chart generation endpoints."""
from fastapi import APIRouter, Query
from charts import (
    create_sales_chart,
    create_revenue_trend,
    create_product_distribution,
    create_price_volume_scatter,
    create_time_series,
    create_multi_line_chart,
    create_stacked_bar_chart,
    create_heatmap,
    create_brush_selection_chart,
    create_boxplot,
    create_histogram,
    create_area_chart,
    create_grouped_bar_chart,
    create_waterfall_chart,
    create_treemap,
    create_radar_chart,
    create_candlestick_chart
)

router = APIRouter(prefix="/api/charts", tags=["dynamic-charts"])


@router.get("/sales-by-region")
async def sales_by_region():
    """Generate horizontal bar chart showing sales by region."""
    return create_sales_chart()


@router.get("/revenue-trend")
async def revenue_trend():
    """Generate line chart showing monthly revenue trend."""
    return create_revenue_trend()


@router.get("/product-distribution")
async def product_distribution():
    """Generate pie chart showing product category distribution."""
    return create_product_distribution()


@router.get("/price-volume-scatter")
async def price_volume_scatter():
    """Generate scatter plot showing price vs volume correlation."""
    return create_price_volume_scatter()


@router.get("/time-series")
async def time_series(days: int = Query(default=30, ge=1, le=365, description="Number of days to display")):
    """Generate time series chart with configurable date range."""
    return create_time_series(days)


@router.get("/multi-line")
async def multi_line():
    """Generate multi-line chart with interactive legend."""
    return create_multi_line_chart()


@router.get("/stacked-bar")
async def stacked_bar():
    """Generate stacked bar chart for composition analysis."""
    return create_stacked_bar_chart()


@router.get("/heatmap")
async def heatmap():
    """Generate heatmap showing activity patterns."""
    return create_heatmap()


@router.get("/brush-selection")
async def brush_selection():
    """Generate brush selection chart for zooming."""
    return create_brush_selection_chart()


@router.get("/boxplot")
async def boxplot():
    """Generate box plot for distribution analysis."""
    return create_boxplot()


@router.get("/histogram")
async def histogram():
    """Generate histogram for frequency distribution."""
    return create_histogram()


@router.get("/area-chart")
async def area_chart():
    """Generate area chart for cumulative trends."""
    return create_area_chart()


@router.get("/grouped-bar")
async def grouped_bar():
    """Generate grouped bar chart for comparison."""
    return create_grouped_bar_chart()


@router.get("/waterfall")
async def waterfall():
    """Generate waterfall chart for sequential changes."""
    return create_waterfall_chart()


@router.get("/treemap")
async def treemap():
    """Generate treemap for hierarchical data."""
    return create_treemap()


@router.get("/radar")
async def radar():
    """Generate radar chart for multivariate comparison."""
    return create_radar_chart()


@router.get("/candlestick")
async def candlestick():
    """Generate candlestick chart for OHLC financial data."""
    return create_candlestick_chart()
