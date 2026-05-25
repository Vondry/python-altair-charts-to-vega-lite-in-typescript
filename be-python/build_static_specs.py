"""Build script to generate static Vega-Lite specifications at build time."""
import json
from pathlib import Path
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

# Create static_specs directory
STATIC_DIR = Path(__file__).parent / "static_specs"
STATIC_DIR.mkdir(exist_ok=True)

# Generate all static specs
specs = {
    "sales-by-region": create_sales_chart(),
    "revenue-trend": create_revenue_trend(),
    "product-distribution": create_product_distribution(),
    "price-volume-scatter": create_price_volume_scatter(),
    "time-series-30": create_time_series(30),
    "time-series-90": create_time_series(90),
    "multi-line": create_multi_line_chart(),
    "stacked-bar": create_stacked_bar_chart(),
    "heatmap": create_heatmap(),
    "brush-selection": create_brush_selection_chart(),
    "boxplot": create_boxplot(),
    "histogram": create_histogram(),
    "area-chart": create_area_chart(),
    "grouped-bar": create_grouped_bar_chart(),
    "waterfall": create_waterfall_chart(),
    "treemap": create_treemap(),
    "radar": create_radar_chart(),
    "candlestick": create_candlestick_chart(),
}

# Write each spec to a JSON file
for name, spec in specs.items():
    file_path = STATIC_DIR / f"{name}.json"
    with open(file_path, 'w') as f:
        json.dump(spec, f, indent=2)
    print(f"✓ Generated {file_path}")

print(f"\n✅ Generated {len(specs)} static Vega-Lite specifications in {STATIC_DIR}")
