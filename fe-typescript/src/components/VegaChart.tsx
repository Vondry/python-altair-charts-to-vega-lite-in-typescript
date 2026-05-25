/**
 * VegaChart component for rendering Vega-Lite visualizations
 */
import {VegaEmbed} from 'react-vega';
import {useChartSpec} from '../hooks/useChartData';
import {API_BASE_URL, BADGE_CONFIG, type ChartMode} from '../config/constants';
import {ChartSkeleton} from './ChartSkeleton';
import {ChartError} from './ChartError';
import type {EmbedOptions} from "vega-embed";

interface VegaChartProps {
    /** Chart endpoint URL */
    url: string;
    /** Chart title */
    title: string;
    /** Rendering mode (charts or data) */
    mode: ChartMode;
}


const options: EmbedOptions = {actions: false}

/**
 * Renders a Vega-Lite chart with loading and error states
 */
export function VegaChart({url, title, mode}: VegaChartProps) {
    const {data: spec, isLoading, error} = useChartSpec(url);

    if (isLoading) {
        return <ChartSkeleton/>;
    }

    if (error) {
        return <ChartError error={error}/>;
    }

    if (!spec) {
        return null;
    }

    const badgeConfig = BADGE_CONFIG[mode];

    return (
        <div className="bg-white rounded-lg border border-gray-200 p-6 shadow-sm">
            <div className="flex items-center gap-2 mb-4">
                <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
                <a
                    href={`${API_BASE_URL}${url}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-400 hover:text-gray-600 transition-colors"
                    title={badgeConfig.tooltip}
                    aria-label={`View ${badgeConfig.text.toLowerCase()} specification`}
                >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                              d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                    </svg>
                </a>
                <span
                    className={`ml-auto text-xs ${badgeConfig.className} px-2 py-1 rounded`}
                    aria-label={`${badgeConfig.text} chart`}
                >
          {badgeConfig.text}
        </span>
            </div>
            <div className="min-w-full min-h-88">
                <VegaEmbed spec={spec} options={options}/>
            </div>
        </div>
    );
}
