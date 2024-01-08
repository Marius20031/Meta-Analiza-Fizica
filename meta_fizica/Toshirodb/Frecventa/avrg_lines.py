import os
from collections import Counter
import matplotlib.pyplot as plt

# Function to read all columns from a file
def read_all_columns(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [list(map(float, line.split())) for line in lines]

# Function to calculate average values across files
def calculate_average_values(file_paths):
    column_sums = Counter()
    column_counts = Counter()

    for file_path in file_paths:
        columns = read_all_columns(file_path)
        for index, row in enumerate(columns):
            key = f"{index + 1}"  # Assuming columns are indexed from 1
            column_sums[key] += sum(row)
            column_counts[key] += len(row)

    average_values = {key: column_sums[key] / column_counts[key] for key in column_sums.keys()}
    return average_values

# Function to plot the bar graph with horizontal lines
def plot_bar_graph(average_values):
    keys = list(average_values.keys())
    values = list(average_values.values())

    fig, ax = plt.subplots()
    ax.bar(keys, values, color='blue')
    ax.set_xlabel('Line')
    ax.set_ylabel('Average Values')
    ax.set_title('Average Values Across Files')

    # Adding horizontal lines from 1 to 4 on the y-axis
    for y_value in range(1, 5):
        ax.axhline(y=y_value, color='red', linestyle='--', linewidth=1)	

    plt.show()

# Main function
def main():
    # Assuming your files are named file_1, file_2, ..., file_13
    file_paths = [f'file_{i}.txt' for i in range(1, 14)]

    # Calculate average values
    average_values = calculate_average_values(file_paths)

    # Display the average values
    print("Average values:")
    for key, value in average_values.items():
        print(f"{key}: {value}")

    # Plot the bar graph
    plot_bar_graph(average_values)

if __name__ == "__main__":
    main()
