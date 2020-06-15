import argparse

from Graph import Graph
from ImageProcessing import IP

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=
        'Image Coloring with Connected-component Labeling, Neighborhood Component and Graph Coloring Algorithms.'
        )
    parser.add_argument('--input', help='Path to input image.', default='teh.png')
    args = parser.parse_args()

    print("Processing Input Image ...", end=" ")
    ip = IP(args.input)

    print("Calculating Adjacency Matrix ...", end=" ")
    matrix = ip.adjacency_matrix()

    print("Graph Coloring ...", end=" ")
    g = Graph(matrix[0].__len__(), matrix)
    colors = g.coloring()
    print("Press a Key To Continue.")
    ip.show(colors)
