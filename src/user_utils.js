export const getStatusColor = (status) => {
  const colors = {
    success: '#28a745',
    warning: '#ffc107',
    error: '#dc3545',
    info: '#17a2b8'
  };
  return colors[status.toLowerCase()] || '#6c757d';
};

export const validateAge = (age) => {
  if (typeof age !== 'number') return false;
  return age >= 18 && age <= 120;
};

export const formatCurrency = (amount, currency = 'USD') => {
  if (isNaN(amount)) return '$0.00';
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currency,
  }).format(amount);
};