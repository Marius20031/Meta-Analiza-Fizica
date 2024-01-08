import os
from collections import Counter
import matplotlib.pyplot as plt

# Function to read all columns from a file
def read_all_columns(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [list(map(float, line.split())) for line in lines]

# Function to calculate frequency of all data values across files
def calculate_frequency_all_data(file_paths):
    all_values = []

    for file_path in file_paths:
        columns = read_all_columns(file_path)
        for row in columns:
            all_values.extend(row)

    frequency_counter = Counter(all_values)
    return frequency_counter

# Function to plot the bar graph with horizontal lines
def plot_bar_graph(frequency_counter):
    values = list(frequency_counter.keys())
    frequencies = list(frequency_counter.values())

    fig, ax = plt.subplots()
    ax.bar(values, frequencies, color='blue')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of All Data Values Across Files')

    # Adding horizontal lines from 1 to 4 on the y-axis
    for y_value in range(1, 5):
        ax.axhline(y=y_value, color='red', linestyle='--', linewidth=1)

    plt.show()

# Main function
def main():
    # Assuming your files are named file_1, file_2, ..., file_13
    file_paths = [f'file_{i}.txt' for i in range(1, 14)]

    # Calculate frequency of all data values
    frequency_counter = calculate_frequency_all_data(file_paths)

    # Display the frequency of all data values
    print("Frequency of all data values:")
    for value, frequency in frequency_counter.items():
        print(f"{value}: {frequency}")

    # Plot the bar graph
    plot_bar_graph(frequency_counter)

if __name__ == "__main__":
    main()
