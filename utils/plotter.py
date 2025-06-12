# utils/plotter.py

import matplotlib.pyplot as plt

def plot_salary_bonus(emp):
    labels = ['Salary', 'Bonus']
    values = [emp.salary, emp.bonus]
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title(f"Salary vs Bonus for {emp.name}")
    plt.ylabel('Amount')
    plt.show()
