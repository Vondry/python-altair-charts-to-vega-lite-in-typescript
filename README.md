# Chart Demo: Altair → Vega-Lite → React

A demonstration application showcasing the **Altair (Python) → Vega-Lite JSON → vega-embed (React)** charting pipeline. The backend exposes multiple REST endpoints, each generating a different chart type using Altair and returning a Vega-Lite specification as JSON. The frontend React app consumes these endpoints and renders the charts client-side using vega-embed, with full TypeScript type safety.

## What This Demonstrates

- **Clean separation**: Chart logic (Python/backend) vs rendering (TypeScript/frontend)
- **Schema-defined contract**: Vega-Lite JSON as the interface
- **Extensibility**: Add new chart types without frontend deployments

## Project Structure

```
charts/
├── be-python/          # FastAPI backend
│   ├── main.py         # API routes
│   ├── charts.py       # Chart generation with Altair
│   ├── data.py         # Sample data generators
│   └── requirements.txt
└── fe-typescript/      # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── VegaChart.tsx       # Reusable chart component
    │   │   └── ChartDashboard.tsx  # Main dashboard
    │   ├── types/
    │   │   └── chart.ts            # TypeScript interfaces
    │   └── App.tsx
    └── package.json
```

## Technology Stack

### Backend (Python)
- **FastAPI** - Async REST framework with automatic OpenAPI docs
- **Altair** - Declarative visualization library (builds Vega-Lite specs)
- **Pandas** - Data manipulation for sample datasets
- **Uvicorn** - ASGI server

### Frontend (TypeScript/React)
- **React 18** with TypeScript
- **Vite** - Build tool
- **react-vega** - Official React wrapper for vega-embed
- **Tailwind CSS** - Styling

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd be-python
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000` with automatic docs at `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd fe-typescript
   ```

2. **Install dependencies:**
   ```bash
   pnpm install
   ```

3. **Start the development server:**
   ```bash
   pnpm dev
   ```

   The app will be available at `http://localhost:5173`

## Available Chart Endpoints

The backend exposes the following REST endpoints:

| Endpoint | Chart Type | Description |
|----------|------------|-------------|
| `GET /api/charts/sales-by-region` | Horizontal Bar Chart | Sales comparison across regions |
| `GET /api/charts/revenue-trend` | Line Chart | Monthly revenue over time |
| `GET /api/charts/product-distribution` | Pie/Donut Chart | Product category breakdown |
| `GET /api/charts/price-volume-scatter` | Scatter Plot | Price vs volume correlation |
| `GET /api/charts/time-series?days=30` | Time Series | Parameterized time-series chart |

### Example Response

Each endpoint returns a Vega-Lite specification as JSON:

```json
{
  "config": { "view": { "continuousWidth": 300, "continuousHeight": 300 } },
  "data": { "name": "data-..." },
  "mark": { "type": "bar" },
  "encoding": {
    "x": { "field": "sales", "type": "quantitative", "title": "Sales ($)" },
    "y": { "field": "region", "type": "nominal", "title": "Region" },
    "color": { "field": "region", "type": "nominal", "legend": null }
  },
  "title": "Sales by Region",
  "width": "container",
  "height": 300
}
```

## Usage

1. **Start both servers** (backend on port 8000, frontend on port 5173)
2. **Open your browser** to `http://localhost:5173`
3. **View the dashboard** displaying all chart types

The frontend automatically fetches chart specifications from the backend and renders them using vega-embed.

## Development Workflow

### Adding a New Chart Type

**Backend (Python):**

1. Add a data generator function in `data.py`
2. Create a chart function in `charts.py` using Altair
3. Add a new endpoint in `main.py`

**Frontend (TypeScript):**

1. Add a new `<VegaChart>` component instance in `ChartDashboard.tsx` pointing to your new endpoint

That's it! No frontend logic changes needed.

### Testing Individual Endpoints

You can test backend endpoints directly:

```bash
# Test an endpoint
curl http://localhost:8000/api/charts/sales-by-region

# Validate the spec in Vega Editor
# Copy the JSON output and paste into https://vega.github.io/editor/
```

## Key Features

- **Responsive charts**: Uses `width: 'container'` for fluid layouts
- **Type safety**: TypeScript validation on Vega-Lite specs
- **Error handling**: Loading states and error boundaries
- **CORS enabled**: For local development across different ports
- **Auto-validation**: Altair validates specs against Vega-Lite schema

## API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## License

MIT
