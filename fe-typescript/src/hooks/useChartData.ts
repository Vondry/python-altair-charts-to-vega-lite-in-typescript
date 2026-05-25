/**
 * Custom hooks for fetching chart data using TanStack Query
 */
import {useQuery} from '@tanstack/react-query';
import {API_BASE_URL, API_ENDPOINTS} from '../config/constants';
import type {ChartMode} from '../config/constants';
import type {VisualizationSpec} from 'vega-embed';
import type {ChartSetResponse} from '../types/api';

/**
 * Constructs the full API URL for a given path
 */
const getApiUrl = (path: string): string => `${API_BASE_URL}${path}`;

/**
 * Hook to fetch a Vega-Lite chart specification
 *
 * @param url - The chart endpoint URL (e.g., '/api/charts/sales-by-region')
 * @returns Query result containing the Vega-Lite spec
 */
export function useChartSpec(url: string) {
    return useQuery<VisualizationSpec, Error>({
        queryKey: ['chart-spec', url],
        queryFn: async () => {
            const response = await fetch(getApiUrl(url));

            if (!response.ok) {
                throw new Error(`Failed to fetch chart: ${response.status} ${response.statusText}`);
            }

            return response.json();
        },
    });
}

/**
 * Hook to fetch chart set metadata
 *
 * @param mode - The chart mode ('charts' for dynamic, 'data' for static)
 * @returns Query result containing the chart set metadata
 */
export function useChartSet(mode: ChartMode) {
    const endpoint = mode === 'charts'
        ? API_ENDPOINTS.CHART_SETS.CHARTS
        : API_ENDPOINTS.CHART_SETS.DATA;

    return useQuery<ChartSetResponse, Error>({
        queryKey: ['chart-set', mode],
        queryFn: async () => {
            const response = await fetch(getApiUrl(endpoint));

            if (!response.ok) {
                throw new Error(`Failed to fetch chart set: ${response.status} ${response.statusText}`);
            }

            return response.json();
        },
    });
}
