/**
 * Main dashboard component displaying chart categories and visualizations
 */
import {useState} from 'react';
import {VegaChart} from './VegaChart';
import {ModeSelector} from './ModeSelector';
import {useChartSet} from '../hooks/useChartData';
import {CHART_MODES, type ChartMode} from '../config/constants';

/**
 * Dashboard component that manages chart display and mode switching
 */
export function ChartDashboard() {
    const [mode, setMode] = useState<ChartMode>(CHART_MODES.CHARTS);
    const {data: chartSet, isLoading, error} = useChartSet(mode);

    return (
        <div className="min-h-screen bg-gray-50 py-8 px-4">
            <div className="max-w-400 mx-auto">
                <header className="mb-6">
                    <h1 className="text-3xl font-bold text-gray-900 mb-2">
                        Chart Demo: Altair → Vega-Lite → React
                    </h1>
                    <p className="text-gray-600 mb-4">
                        Comprehensive visualization library with 17+ chart types
                    </p>
                    <ModeSelector mode={mode} onModeChange={setMode}/>
                    <p className="text-sm text-gray-500 mt-4">
                        ✨ Interactive features: Click legends, brush to zoom, hover for details
                    </p>
                </header>

                {isLoading ? (
                    <div className="text-center py-12">
                        <div
                            className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
                        <p className="mt-4 text-gray-600">Loading charts...</p>
                    </div>
                ) : error ? (
                    <div className="text-center py-12 text-red-600">
                        Failed to load chart set: {error.message}
                    </div>
                ) : chartSet ? (
                    chartSet.categories.map(({title, charts}) => (
                        <section key={title} className="mb-12">
                            <h2 className="text-2xl font-semibold text-gray-800 mb-4">{title}</h2>
                            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">
                                {charts.map(({url, title}) => (
                                    <VegaChart key={url} url={url} title={title} mode={mode}/>
                                ))}
                            </div>
                        </section>
                    ))
                ) : null}
            </div>
        </div>
    );
}
