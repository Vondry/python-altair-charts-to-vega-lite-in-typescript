/**
 * Mode selector component for switching between chart rendering modes
 */
import { CHART_MODES, type ChartMode } from '../config/constants';

interface ModeSelectorProps {
  /** Current selected mode */
  mode: ChartMode;
  /** Callback when mode changes */
  onModeChange: (mode: ChartMode) => void;
}

/**
 * Renders a toggle for switching between dynamic and static chart modes
 */
export function ModeSelector({ mode, onModeChange }: ModeSelectorProps) {
  const isDynamicMode = mode === CHART_MODES.CHARTS;
  const isStaticMode = mode === CHART_MODES.DATA;

  return (
    <div className="flex items-center gap-4 bg-white rounded-lg border border-gray-200 p-4 shadow-sm">
      <span className="text-sm font-medium text-gray-700">Mode:</span>
      <div className="flex gap-2">
        <button
          onClick={() => onModeChange(CHART_MODES.CHARTS)}
          className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
            isDynamicMode
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
          aria-pressed={isDynamicMode}
          aria-label="Switch to dynamic generation mode"
        >
          ⚡ Dynamic Generation
        </button>
        <button
          onClick={() => onModeChange(CHART_MODES.DATA)}
          className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
            isStaticMode
              ? 'bg-green-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
          aria-pressed={isStaticMode}
          aria-label="Switch to static pre-built mode"
        >
          📦 Static Pre-built
        </button>
      </div>
      <div className="ml-auto text-xs text-gray-500">
        {isDynamicMode ? (
          <span>Altair generates specs on-demand</span>
        ) : (
          <span>Pre-built specs from build time</span>
        )}
      </div>
    </div>
  );
}