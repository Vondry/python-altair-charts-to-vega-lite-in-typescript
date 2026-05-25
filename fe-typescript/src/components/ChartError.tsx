/**
 * Error display component for chart loading failures
 */
interface ChartErrorProps {
  error: Error;
}

/**
 * Displays a user-friendly error message when chart loading fails
 */
export function ChartError({ error }: ChartErrorProps) {
  return (
    <div className="p-8 bg-red-50 rounded-lg border border-red-200">
      <div className="text-red-800 font-semibold">Error Loading Chart</div>
      <div className="text-red-600 text-sm mt-1">{error.message}</div>
    </div>
  );
}
