import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

const LineChart = ({ data }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  console.log(data);
  useEffect(() => {
    try {
      const parsedData = JSON.parse(data);

      if (chartInstance.current) {
        // Destroy the existing chart instance
        chartInstance.current.destroy();
      }

      const labels = Object.keys(parsedData);
      const datasets = Object.keys(parsedData[labels[0]]).map(key => ({
        label: key,
        data: labels.map(month => parsedData[month][key]),
        fill: false,
        borderColor: '#' + (0x1000000 + (Math.random()) * 0xffffff).toString(16).substr(1, 6) // Random color
      }));

      const ctx = chartRef.current.getContext('2d');

      // Create new chart instance
      chartInstance.current = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: datasets
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });

      // Cleanup function to destroy the chart when component unmounts
      return () => {
        if (chartInstance.current) {
          chartInstance.current.destroy();
        }
      };
    } catch (error) {
      console.error('Error parsing JSON data:', error);
    }
  }, [data]);

  return <canvas ref={chartRef} />;
};

export default LineChart;
