import statistics
import matplotlib.pyplot as plt

def mini_meta_analysis(data):
    results = []

    for line in data:
        # Split the line into name and values
        parts = line.split()
        name = parts[0]
        values = list(map(float, parts[1:]))

        # Calculate mean and standard deviation
        mean_value = statistics.mean(values)
        std_deviation = statistics.stdev(values)

        # Store results in a tuple
        results.append((name, mean_value, std_deviation))

    return results

def plot_graph(results):
    names = [result[0] for result in results]
    mean_values = [result[1] for result in results]

    plt.bar(names, mean_values, color='blue', alpha=0.7)
    plt.xlabel('Names')
    plt.ylabel('Mean Values')
    plt.title('Mini Meta-Analysis - Mean Values')

    # Set y-axis limits to zoom in on the range around 50
    plt.ylim(53, 55)

    # Set y-axis ticks to show values around 50
    plt.yticks(range(53, 56, 1))

    plt.show()

# Rest of the code remains unchanged

def main():
    file_name = "input.txt"

    try:
        with open(file_name, 'r') as file:
            data = file.readlines()

        meta_analysis_results = mini_meta_analysis(data)

        # Display the results
        print("Mini Meta-Analysis Results:")
        print("Name\tMean\tStandard Deviation")
        for result in meta_analysis_results:
            print(f"{result[0]}\t{result[1]:.2f}\t{result[2]:.2f}")

        # Plot the graph
        plot_graph(meta_analysis_results)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
