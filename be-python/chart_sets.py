"""Chart set metadata for charts and data rendering modes."""

STATIC_CHART_SET = {
    "mode": "charts",
    "description": "Dynamic: Backend generates Vega-Lite specs with Altair on-demand",
    "categories": [
        {
            "title": "📊 Basic Charts",
            "charts": [
                {"url": "/api/charts/sales-by-region", "title": "Sales by Region (Bar)", "type": "bar"},
                {"url": "/api/charts/revenue-trend", "title": "Revenue Trend (Line)", "type": "line"},
                {"url": "/api/charts/product-distribution", "title": "Product Distribution (Pie)", "type": "pie"},
                {"url": "/api/charts/price-volume-scatter", "title": "Price vs Volume (Scatter)", "type": "scatter"}
            ]
        },
        {
            "title": "🎯 Interactive Charts",
            "charts": [
                {"url": "/api/charts/multi-line", "title": "Product Comparison (Click legend)", "type": "multi-line"},
                {"url": "/api/charts/stacked-bar", "title": "Revenue by Channel (Stacked)", "type": "stacked-bar"},
                {"url": "/api/charts/heatmap", "title": "Activity Heatmap", "type": "heatmap"},
                {"url": "/api/charts/brush-selection", "title": "Time Series (Brush to zoom)", "type": "brush"}
            ]
        },
        {
            "title": "📈 Statistical Charts",
            "charts": [
                {"url": "/api/charts/boxplot", "title": "Distribution (Box Plot)", "type": "boxplot"},
                {"url": "/api/charts/histogram", "title": "Frequency (Histogram)", "type": "histogram"},
                {"url": "/api/charts/area-chart", "title": "Cumulative Revenue (Area)", "type": "area"}
            ]
        },
        {
            "title": "🔄 Comparison Charts",
            "charts": [
                {"url": "/api/charts/grouped-bar", "title": "Year Comparison (Grouped Bar)", "type": "grouped-bar"},
                {"url": "/api/charts/waterfall", "title": "Financial Flow (Waterfall)", "type": "waterfall"}
            ]
        },
        {
            "title": "🌳 Hierarchical & Specialized",
            "charts": [
                {"url": "/api/charts/treemap", "title": "Sales Breakdown (Treemap)", "type": "treemap"},
                {"url": "/api/charts/radar", "title": "Product Metrics (Radar)", "type": "radar"},
                {"url": "/api/charts/candlestick", "title": "Stock Price (Candlestick)", "type": "candlestick"}
            ]
        },
        {
            "title": "⏱️ Time Series",
            "charts": [
                {"url": "/api/charts/time-series?days=30", "title": "Last 30 Days", "type": "time-series"},
                {"url": "/api/charts/time-series?days=90", "title": "Last 90 Days", "type": "time-series"}
            ]
        }
    ]
}

DYNAMIC_CHART_SET = {
    "mode": "data",
    "description": "Static: Pre-built Vega-Lite specs generated at build time",
    "categories": [
        {
            "title": "📊 Basic Charts",
            "charts": [
                {"url": "/api/data/sales-by-region", "title": "Sales by Region (Bar)", "type": "bar"},
                {"url": "/api/data/revenue-trend", "title": "Revenue Trend (Line)", "type": "line"},
                {"url": "/api/data/product-distribution", "title": "Product Distribution (Pie)", "type": "pie"},
                {"url": "/api/data/price-volume-scatter", "title": "Price vs Volume (Scatter)", "type": "scatter"}
            ]
        },
        {
            "title": "🎯 Interactive Charts",
            "charts": [
                {"url": "/api/data/multi-line", "title": "Product Comparison (Click legend)", "type": "multi-line"},
                {"url": "/api/data/stacked-bar", "title": "Revenue by Channel (Stacked)", "type": "stacked-bar"},
                {"url": "/api/data/heatmap", "title": "Activity Heatmap", "type": "heatmap"},
                {"url": "/api/data/brush-selection", "title": "Time Series (Brush to zoom)", "type": "brush"}
            ]
        },
        {
            "title": "📈 Statistical Charts",
            "charts": [
                {"url": "/api/data/boxplot", "title": "Distribution (Box Plot)", "type": "boxplot"},
                {"url": "/api/data/histogram", "title": "Frequency (Histogram)", "type": "histogram"},
                {"url": "/api/data/area-chart", "title": "Cumulative Revenue (Area)", "type": "area"}
            ]
        },
        {
            "title": "🔄 Comparison Charts",
            "charts": [
                {"url": "/api/data/grouped-bar", "title": "Year Comparison (Grouped Bar)", "type": "grouped-bar"},
                {"url": "/api/data/waterfall", "title": "Financial Flow (Waterfall)", "type": "waterfall"}
            ]
        },
        {
            "title": "🌳 Hierarchical & Specialized",
            "charts": [
                {"url": "/api/data/treemap", "title": "Sales Breakdown (Treemap)", "type": "treemap"},
                {"url": "/api/data/radar", "title": "Product Metrics (Radar)", "type": "radar"},
                {"url": "/api/data/candlestick", "title": "Stock Price (Candlestick)", "type": "candlestick"}
            ]
        },
        {
            "title": "⏱️ Time Series",
            "charts": [
                {"url": "/api/data/time-series?days=30", "title": "Last 30 Days", "type": "time-series"},
                {"url": "/api/data/time-series?days=90", "title": "Last 90 Days", "type": "time-series"}
            ]
        }
    ]
}