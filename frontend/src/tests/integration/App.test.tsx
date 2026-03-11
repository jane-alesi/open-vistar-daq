import { render, screen } from '@testing-library/react';
import App from '../../App';
import { expect, test } from 'vitest';

test('renders the main dashboard title', () => {
  render(<App />);
  const titleElement = screen.getByText(/Open Vistar DAQ/i);
  expect(titleElement).toBeInTheDocument();
});

test('renders the visualization container', () => {
  render(<App />);
  const containerElement = screen.getByTestId('vistar-container');
  expect(containerElement).toBeInTheDocument();
});
