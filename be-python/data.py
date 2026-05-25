"""Sample data generators for chart demonstrations."""
import pandas as pd
from datetime import datetime, timedelta
import random

# Static datasets
SALES_DATA = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West', 'Central'],
    'sales': [45000, 38000, 52000, 41000, 47000]
})

REVENUE_DATA = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'revenue': [120000, 135000, 142000, 138000, 155000, 168000, 175000, 182000, 178000, 190000, 195000, 210000]
})

PRODUCT_DATA = pd.DataFrame({
    'category': ['Electronics', 'Clothing', 'Food', 'Books', 'Home & Garden'],
    'value': [35, 25, 20, 12, 8]
})


def get_scatter_data():
    """Generate price vs volume scatter data."""
    random.seed(42)
    prices = [random.uniform(10, 100) for _ in range(50)]
    return pd.DataFrame({
        'price': prices,
        'volume': [int(1000 - p * 8 + random.uniform(-100, 100)) for p in prices],
        'category': [random.choice(['A', 'B', 'C']) for _ in range(50)]
    })


def get_time_series(days: int = 30):
    """Generate time series data."""
    random.seed(42)
    start = datetime.now() - timedelta(days=days)
    return pd.DataFrame({
        'date': [start + timedelta(days=i) for i in range(days)],
        'value': [100 + sum(random.uniform(-5, 5) for _ in range(i+1)) for i in range(days)]
    })


def get_multi_line_data():
    """Generate multi-line time series for comparison."""
    random.seed(42)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data = []
    for product in ['Product A', 'Product B', 'Product C']:
        base = random.randint(50, 150)
        for i, month in enumerate(months):
            data.append({
                'month': month,
                'sales': base + random.randint(-20, 30) + i * 5,
                'product': product
            })
    return pd.DataFrame(data)


def get_stacked_bar_data():
    """Generate stacked bar chart data."""
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    categories = ['Online', 'Retail', 'Wholesale']
    data = []
    random.seed(42)
    for quarter in quarters:
        for category in categories:
            data.append({
                'quarter': quarter,
                'channel': category,
                'revenue': random.randint(20000, 80000)
            })
    return pd.DataFrame(data)


def get_heatmap_data():
    """Generate heatmap data."""
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hours = list(range(9, 18))
    data = []
    random.seed(42)
    for day in days:
        for hour in hours:
            data.append({
                'day': day,
                'hour': f'{hour}:00',
                'activity': random.randint(10, 100)
            })
    return pd.DataFrame(data)


def get_brush_data():
    """Generate data for brush selection chart."""
    random.seed(42)
    dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
    return pd.DataFrame({
        'date': dates,
        'value': [100 + sum(random.uniform(-3, 3) for _ in range(i+1)) for i in range(365)]
    })


def get_boxplot_data():
    """Generate data for box plot."""
    random.seed(42)
    data = []
    for species in ['Setosa', 'Versicolor', 'Virginica']:
        base = random.uniform(4, 7)
        for _ in range(50):
            data.append({
                'species': species,
                'value': base + random.gauss(0, 0.5)
            })
    return pd.DataFrame(data)


def get_histogram_data():
    """Generate data for histogram."""
    random.seed(42)
    return pd.DataFrame({
        'value': [random.gauss(100, 20) for _ in range(200)]
    })


def get_area_data():
    """Generate data for area chart."""
    random.seed(42)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return pd.DataFrame({
        'month': months,
        'revenue': [50000 + i * 5000 + random.randint(-5000, 5000) for i in range(12)]
    })


def get_grouped_bar_data():
    """Generate data for grouped bar chart."""
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    data = []
    random.seed(42)
    for cat in categories:
        for year in ['2023', '2024']:
            data.append({
                'quarter': cat,
                'year': year,
                'revenue': random.randint(40000, 90000)
            })
    return pd.DataFrame(data)


def get_waterfall_data():
    """Generate data for waterfall chart."""
    return pd.DataFrame({
        'category': ['Starting', 'Revenue', 'Costs', 'Marketing', 'R&D', 'Ending'],
        'amount': [100000, 50000, -20000, -15000, -10000, 105000],
        'type': ['total', 'increase', 'decrease', 'decrease', 'decrease', 'total']
    })


def get_treemap_data():
    """Generate hierarchical data for treemap."""
    data = []
    categories = {
        'Electronics': ['Phones', 'Laptops', 'Tablets'],
        'Clothing': ['Shirts', 'Pants', 'Shoes'],
        'Food': ['Snacks', 'Beverages', 'Frozen']
    }
    random.seed(42)
    for parent, children in categories.items():
        for child in children:
            data.append({
                'category': parent,
                'subcategory': child,
                'value': random.randint(1000, 5000)
            })
    return pd.DataFrame(data)


def get_radar_data():
    """Generate data for radar chart."""
    return pd.DataFrame({
        'metric': ['Speed', 'Quality', 'Cost', 'Reliability', 'Innovation', 'Support'],
        'Product A': [8, 7, 6, 9, 7, 8],
        'Product B': [6, 9, 8, 7, 8, 7]
    })


def get_candlestick_data():
    """Generate OHLC data for candlestick chart."""
    random.seed(42)
    dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(30)]
    data = []
    price = 100
    for date in dates:
        open_price = price
        high = open_price + random.uniform(0, 5)
        low = open_price - random.uniform(0, 5)
        close = random.uniform(low, high)
        data.append({
            'date': date,
            'open': open_price,
            'high': high,
            'low': low,
            'close': close
        })
        price = close
    return pd.DataFrame(data)