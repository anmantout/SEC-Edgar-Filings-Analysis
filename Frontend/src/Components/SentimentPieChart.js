import React from 'react';
import { Pie } from 'react-chartjs-2';

const SentimentPieChart = ({ data }) => {
  const { positive, negative, neutral } = data;
  console.log(positive,negative,neutral);
  console.log(data);
  const chartData = {
    labels: ['Positive', 'Negative', 'Neutral'],
    datasets: [
      {
        label: 'Sentiment Distribution',
        data: [positive, negative, neutral],
        backgroundColor: [
          'rgba(75, 192, 192, 0.6)', // Positive
          'rgba(255, 99, 132, 0.6)', // Negative
          'rgba(255, 206, 86, 0.6)', // Neutral
        ],
        borderColor: [
          'rgba(75, 192, 192, 1)', // Positive
          'rgba(255, 99, 132, 1)', // Negative
          'rgba(255, 206, 86, 1)', // Neutral
        ],
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
      },
    },
  };

  return (
    <div style={{ height: '400px', width: '400px' }}>
      <Pie data={chartData} options={chartOptions} />
    </div>
  );
};

export default SentimentPieChart;
