// script.js

// Pie Chart: Income vs Expense
const pieCtx = document.getElementById('pieChart').getContext('2d');
const pieChart = new Chart(pieCtx, {
    type: 'pie',
    data: {
        labels: ['Income', 'Expense'],
        datasets: [{
            data: [50000, 25000], 
            backgroundColor: ['#2ecc71', '#e74c3c']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top'
            },
            datalabels: {
                color: '#fff',
                font: {
                    size: 14,
                    weight: 'bold'
                },
                formatter: (value) => `₹${value}` 
            }
        }
    },
    plugins: [ChartDataLabels]
});

// Bar Chart: Categories
const barCtx = document.getElementById('barChart').getContext('2d');
const barChart = new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: ['Groceries', 'Transportation', 'Entertainment', 'Bills', 'Miscellaneous'],
        datasets: [{
            label: 'Expenses',
            data: [2000, 500, 1200, 3000, 800], 
            backgroundColor: '#3498db'
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Categories'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Amount (₹)'
                }
            }
        }
    }
});
