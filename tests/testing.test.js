import { add } from './math';

describe('add function', () => {
  test('should correctly add two positive numbers', () => {
    expect(add(2, 3)).toBe(5);
  });

  test('should correctly add a positive and a negative number', () => {
    expect(add(5, -2)).toBe(3);
  });

  test('should correctly add two negative numbers', () => {
    expect(add(-1, -1)).toBe(-2);
  });

  test('should correctly add zero to a number', () => {
    expect(add(10, 0)).toBe(10);
    expect(add(0, 10)).toBe(10);
  });

  test('should correctly add decimal numbers', () => {
    expect(add(1.5, 2.7)).toBeCloseTo(4.2);
  });
});