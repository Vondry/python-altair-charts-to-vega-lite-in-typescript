/**
 * Application configuration and constants
 */

/** Base URL for the backend API */
export const API_BASE_URL = 'http://localhost:8000';

/** Chart rendering modes */
export const CHART_MODES = {
  CHARTS: 'charts',
  DATA: 'data',
} as const;

/** Chart mode type */
export type ChartMode = typeof CHART_MODES[keyof typeof CHART_MODES];

/** API endpoints */
export const API_ENDPOINTS = {
  CHART_SETS: {
    CHARTS: '/api/chart-sets/charts',
    DATA: '/api/chart-sets/data',
  },
  CHARTS: '/api/charts',
  DATA: '/api/data',
} as const;

/** Query configuration */
export const QUERY_CONFIG = {
  STALE_TIME: 5 * 60 * 1000, // 5 minutes
  GC_TIME: 10 * 60 * 1000, // 10 minutes
  RETRY: 1,
  REFETCH_ON_WINDOW_FOCUS: false,
} as const;

/** Chart badge configuration */
export const BADGE_CONFIG = {
  [CHART_MODES.CHARTS]: {
    className: 'text-blue-600 bg-blue-50',
    text: 'Dynamic',
    tooltip: 'View dynamic Vega-Lite spec',
  },
  [CHART_MODES.DATA]: {
    className: 'text-green-600 bg-green-50',
    text: 'Static',
    tooltip: 'View static Vega-Lite spec',
  },
} as const;