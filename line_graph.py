import pandas as pd
import matplotlib.pyplot as plt
import argparse


def plot_lines_from_csv(file_path: str, arguments: argparse):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Replace non-numeric values with NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Get the first column for x-axis
    x = df.iloc[:, 0]

    # Create a new figure
    plt.figure()

    # Plot each column
    for column in df.columns[1:]:
        # Pair x and y values together and drop pairs with NaN y values
        xy_pairs = df[[df.columns[0], column]].dropna()
        x = xy_pairs.iloc[:, 0]
        y = xy_pairs[column]
        plt.plot(x, y, label=column)

    # Add a legend, title and show the plot
    plt.legend()
    plt.title(arguments.title)
    plt.xlabel('Levels')            # Add x-axis label
    plt.ylabel('Time (seconds)')    # Add y-axis label
    plt.savefig(arguments.graph)


def main():
    parser = argparse.ArgumentParser(prog='A python program that will do line plots for you')

    parser.add_argument('--file', '-f', nargs='?', dest='csv', action='store',
                        help="file name of the CSV", type=str)
    parser.add_argument('--graph', '-g', nargs='?', dest='graph', action='store',
                        help="file name of the output graph", type=str)
    parser.add_argument('--title', '-t', nargs='?', dest='title', action='store',
                        help="title of the output graph", type=str)

    args = parser.parse_args()
    # Call the function with the path to your CSV file
    plot_lines_from_csv(args.csv, args)


if __name__ == '__main__':
    main()
