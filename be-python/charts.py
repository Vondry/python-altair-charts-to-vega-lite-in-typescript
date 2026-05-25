"""Chart generation functions using Altair."""
import altair as alt
from data import (
    SALES_DATA, REVENUE_DATA, PRODUCT_DATA, 
    get_scatter_data, get_time_series, get_multi_line_data,
    get_stacked_bar_data, get_heatmap_data, get_brush_data,
    get_boxplot_data, get_histogram_data, get_area_data,
    get_grouped_bar_data, get_waterfall_data, get_treemap_data,
    get_radar_data, get_candlestick_data
)


def create_sales_chart():
    """Horizontal bar chart: sales by region."""
    return (
        alt.Chart(SALES_DATA)
        .mark_bar()
        .encode(
            x=alt.X('sales:Q', title='Sales ($)'),
            y=alt.Y('region:N', title='Region', sort='-x'),
            color=alt.Color('region:N', legend=None),
            tooltip=['region', 'sales']
        )
        .properties(title='Sales by Region', width=500, height=300)
        .to_dict()
    )


def create_revenue_trend():
    """Line chart: monthly revenue trend."""
    return (
        alt.Chart(REVENUE_DATA)
        .mark_line(point=True)
        .encode(
            x=alt.X('month:N', title='Month', sort=None),
            y=alt.Y('revenue:Q', title='Revenue ($)'),
            tooltip=['month', 'revenue']
        )
        .properties(title='Monthly Revenue Trend', width=500, height=300)
        .to_dict()
    )


def create_product_distribution():
    """Pie chart: product category distribution."""
    return (
        alt.Chart(PRODUCT_DATA)
        .mark_arc(innerRadius=50)
        .encode(
            theta=alt.Theta('value:Q'),
            color=alt.Color('category:N', legend=alt.Legend(title='Category')),
            tooltip=['category', 'value']
        )
        .properties(title='Product Distribution', width=500, height=300)
        .to_dict()
    )


def create_price_volume_scatter():
    """Scatter plot: price vs volume correlation."""
    return (
        alt.Chart(get_scatter_data())
        .mark_circle(size=60)
        .encode(
            x=alt.X('price:Q', title='Price ($)'),
            y=alt.Y('volume:Q', title='Volume'),
            color=alt.Color('category:N', legend=alt.Legend(title='Category')),
            tooltip=['price', 'volume', 'category']
        )
        .properties(title='Price vs Volume', width=500, height=300)
        .to_dict()
    )


def create_time_series(days=30):
    """Time series chart with configurable date range."""
    return (
        alt.Chart(get_time_series(days))
        .mark_line()
        .encode(
            x=alt.X('date:T', title='Date'),
            y=alt.Y('value:Q', title='Value'),
            tooltip=[alt.Tooltip('date:T'), alt.Tooltip('value:Q')]
        )
        .properties(title=f'Time Series ({days} days)', width=500, height=300)
        .to_dict()
    )


def create_multi_line_chart():
    """Multi-line chart with interactive legend."""
    selection = alt.selection_point(fields=['product'], bind='legend')
    
    return (
        alt.Chart(get_multi_line_data())
        .mark_line(point=True)
        .encode(
            x=alt.X('month:N', title='Month', sort=None),
            y=alt.Y('sales:Q', title='Sales'),
            color=alt.Color('product:N', legend=alt.Legend(title='Product')),
            opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
            tooltip=['product', 'month', 'sales']
        )
        .add_params(selection)
        .properties(title='Product Sales Comparison', width=500, height=300)
        .to_dict()
    )


def create_stacked_bar_chart():
    """Stacked bar chart for composition analysis."""
    return (
        alt.Chart(get_stacked_bar_data())
        .mark_bar()
        .encode(
            x=alt.X('quarter:N', title='Quarter'),
            y=alt.Y('revenue:Q', title='Revenue ($)', stack='zero'),
            color=alt.Color('channel:N', legend=alt.Legend(title='Channel')),
            tooltip=['quarter', 'channel', 'revenue']
        )
        .properties(title='Revenue by Channel', width=500, height=300)
        .to_dict()
    )


def create_heatmap():
    """Heatmap for activity patterns."""
    return (
        alt.Chart(get_heatmap_data())
        .mark_rect()
        .encode(
            x=alt.X('hour:N', title='Hour'),
            y=alt.Y('day:N', title='Day', sort=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']),
            color=alt.Color('activity:Q', scale=alt.Scale(scheme='blues'), legend=alt.Legend(title='Activity')),
            tooltip=['day', 'hour', 'activity']
        )
        .properties(title='Activity Heatmap', width=500, height=300)
        .to_dict()
    )


def create_brush_selection_chart():
    """Brush selection chart for zooming."""
    data = get_brush_data()
    brush = alt.selection_interval(encodings=['x'])
    
    upper = alt.Chart(data).mark_line().encode(
        x=alt.X('date:T', scale=alt.Scale(domain=brush), title='Date'),
        y=alt.Y('value:Q', title='Value')
    ).properties(width=500, height=200, title='Brush to Zoom')
    
    lower = alt.Chart(data).mark_line().encode(
        x=alt.X('date:T', title='Date'),
        y=alt.Y('value:Q', title='Value')
    ).add_params(brush).properties(width=500, height=60)
    
    return (upper & lower).to_dict()


def create_boxplot():
    """Box plot for distribution analysis."""
    return (
        alt.Chart(get_boxplot_data())
        .mark_boxplot()
        .encode(
            x=alt.X('species:N', title='Species'),
            y=alt.Y('value:Q', title='Value'),
            color=alt.Color('species:N', legend=None)
        )
        .properties(title='Distribution by Species', width=500, height=300)
        .to_dict()
    )


def create_histogram():
    """Histogram for frequency distribution."""
    return (
        alt.Chart(get_histogram_data())
        .mark_bar()
        .encode(
            x=alt.X('value:Q', bin=alt.Bin(maxbins=30), title='Value'),
            y=alt.Y('count()', title='Frequency'),
            tooltip=[alt.Tooltip('count()')]
        )
        .properties(title='Value Distribution', width=500, height=300)
        .to_dict()
    )


def create_area_chart():
    """Area chart for cumulative trends."""
    return (
        alt.Chart(get_area_data())
        .mark_area(opacity=0.7)
        .encode(
            x=alt.X('month:N', title='Month', sort=None),
            y=alt.Y('revenue:Q', title='Revenue ($)'),
            tooltip=['month', 'revenue']
        )
        .properties(title='Cumulative Revenue', width=500, height=300)
        .to_dict()
    )


def create_grouped_bar_chart():
    """Grouped bar chart for comparison."""
    return (
        alt.Chart(get_grouped_bar_data())
        .mark_bar()
        .encode(
            x=alt.X('quarter:N', title='Quarter'),
            y=alt.Y('revenue:Q', title='Revenue ($)'),
            color=alt.Color('year:N', legend=alt.Legend(title='Year')),
            xOffset='year:N',
            tooltip=['quarter', 'year', 'revenue']
        )
        .properties(title='Year-over-Year Comparison', width=500, height=300)
        .to_dict()
    )


def create_waterfall_chart():
    """Waterfall chart for sequential changes."""
    return (
        alt.Chart(get_waterfall_data())
        .mark_bar()
        .encode(
            x=alt.X('category:N', title='Category', sort=None),
            y=alt.Y('amount:Q', title='Amount ($)'),
            color=alt.Color('type:N', 
                          scale=alt.Scale(domain=['total', 'increase', 'decrease'], 
                                        range=['#4682b4', '#90ee90', '#ff6b6b']),
                          legend=alt.Legend(title='Type')),
            tooltip=['category', 'amount', 'type']
        )
        .properties(title='Financial Waterfall', width=500, height=300)
        .to_dict()
    )


def create_treemap():
    """Treemap for hierarchical data."""
    return (
        alt.Chart(get_treemap_data())
        .mark_rect()
        .encode(
            x=alt.X('sum(value):Q', stack='zero', axis=None),
            y=alt.Y('category:N', axis=None),
            color=alt.Color('category:N', legend=alt.Legend(title='Category')),
            tooltip=['category', 'subcategory', 'value'],
            facet=alt.Facet('subcategory:N', columns=3)
        )
        .properties(title='Sales Treemap', width=150, height=100)
        .to_dict()
    )


def create_radar_chart():
    """Radar chart for multivariate comparison using polar coordinates."""
    data = get_radar_data()
    data_long = data.melt(id_vars=['metric'], var_name='product', value_name='score')
    
    # Create base chart with proper projection
    base = alt.Chart(data_long).encode(
        theta=alt.Theta('metric:N', stack=None),
        radius=alt.Radius('score:Q', scale=alt.Scale(domain=[0, 10], type='linear')),
        color=alt.Color('product:N', legend=alt.Legend(title='Product')),
        tooltip=['product:N', 'metric:N', 'score:Q']
    )
    
    # Layer filled area and line with points
    area = base.mark_arc(innerRadius=0, stroke=None, opacity=0.3)
    line = base.mark_line(point=True, strokeWidth=2)
    
    return (area + line).properties(
        title='Product Comparison Radar',
        width=400,
        height=400
    ).to_dict()


def create_candlestick_chart():
    """Candlestick chart for OHLC financial data."""
    data = get_candlestick_data()
    
    rule = alt.Chart(data).mark_rule().encode(
        x=alt.X('date:T', title='Date'),
        y=alt.Y('low:Q', title='Price ($)', scale=alt.Scale(zero=False)),
        y2='high:Q'
    )
    
    bar = alt.Chart(data).mark_bar().encode(
        x='date:T',
        y='open:Q',
        y2='close:Q',
        color=alt.condition(
            "datum.open <= datum.close",
            alt.value("#06982d"),
            alt.value("#ae1325")
        )
    )
    
    return (rule + bar).properties(title='Stock Price (OHLC)', width=500, height=300).to_dict()
