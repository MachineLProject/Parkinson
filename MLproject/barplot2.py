import matplotlib.pyplot as plt

# Data
algorithms = ['KNN', 'Decision Tree', 'SVM']
sensitivity = [97.5, 95.0, 97.5]
specificity = [63.15, 78.94, 73.68]

# Plotting
plt.figure(figsize=(12, 6))

# Plotting Sensitivity
plt.subplot(1, 2, 1)
plt.bar(algorithms, sensitivity, color='maroon')
plt.title('Sensitivity')
plt.ylim(80, 100)
plt.ylabel('Percentage')

# Plotting Specificity
plt.subplot(1, 2, 2)
plt.bar(algorithms, specificity, color='maroon')
plt.title('Specificity')
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig('barplot2.png')
plt.show()
