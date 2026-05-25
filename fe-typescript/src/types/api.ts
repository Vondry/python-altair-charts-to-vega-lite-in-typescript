/**
 * API response types
 */

/** Chart information in metadata response */
export interface ChartInfo {
  url: string;
  title: string;
  type: string;
}

/** Chart category grouping */
export interface ChartCategory {
  title: string;
  charts: ChartInfo[];
}

/** Chart set metadata response */
export interface ChartSetResponse {
  mode: string;
  description: string;
  categories: ChartCategory[];
}

/** Vega-Lite specification type */
export interface VisualizationSpec {
  $schema?: string;
  data?: unknown;
  mark?: unknown;
  encoding?: unknown;
  layer?: unknown[];
  vconcat?: unknown[];
  hconcat?: unknown[];
  [key: string]: unknown;
}

/** API error response */
export interface ApiError {
  detail: string;
  status?: number;
}
