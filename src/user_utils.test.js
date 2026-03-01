import { getStatusColor, validateAge, formatCurrency } from './utils';

describe('getStatusColor', () => {
  test('returns correct color for success status', () => {
    expect(getStatusColor('success')).toBe('#28a745');
  });

  test('returns correct color for warning status', () => {
    expect(getStatusColor('warning')).toBe('#ffc107');
  });

  test('returns correct color for error status', () => {
    expect(getStatusColor('error')).toBe('#dc3545');
  });

  test('returns correct color for info status', () => {
    expect(getStatusColor('info')).toBe('#17a2b8');
  });

  test('returns default color for unknown status', () => {
    expect(getStatusColor('unknown')).toBe('#6c757d');
  });

  test('handles case insensitive status', () => {
    expect(getStatusColor('SUCCESS')).toBe('#28a745');
  });
});

describe('validateAge', () => {
  test('returns true for valid age within range', () => {
    expect(validateAge(25)).toBe(true);
  });

  test('returns false for age below 18', () => {
    expect(validateAge(17)).toBe(false);
  });

  test('returns false for age above 120', () => {
    expect(validateAge(121)).toBe(false);
  });

  test('returns false for non-number input', () => {
    expect(validateAge('25')).toBe(false);
  });

  test('returns false for null input', () => {
    expect(validateAge(null)).toBe(false);
  });

  test('returns true for boundary value 18', () => {
    expect(validateAge(18)).toBe(true);
  });

  test('returns true for boundary value 120', () => {
    expect(validateAge(120)).toBe(true);
  });
});

describe('formatCurrency', () => {
  test('formats valid number with default USD currency', () => {
    expect(formatCurrency(100)).toBe('$100.00');
  });

  test('formats valid number with specified currency', () => {
    expect(formatCurrency(100, 'EUR')).toBe('€100.00');
  });

  test('returns $0.00 for NaN input', () => {
    expect(formatCurrency(NaN)).toBe('$0.00');
  });

  test('formats decimal numbers correctly', () => {
    expect(formatCurrency(99.99)).toBe('$99.99');
  });

  test('formats negative numbers correctly', () => {
    expect(formatCurrency(-100)).toBe('-$100.00');
  });

  test('formats zero correctly', () => {
    expect(formatCurrency(0)).toBe('$0.00');
  });
});