class Graph():

    def __init__(self, no_v, adj_matrix):
        self.no_v = no_v
        self.matrix = adj_matrix
        self.colors = [0] * no_v

    def coloring(self):
        if self.no_v == 1:
            print("1 Color")
            return [1]  # vertex 0 can be colored with 1

        if self.backtrack(0, 2, self.colors):
            print("2 Colors")
            return self.colors

        if self.backtrack(0, 3, self.colors):
            print("3 Colors")
            return self.colors

        if self.backtrack(0, 4, self.colors):
            print("4 Colors")
            return self.colors

        return False

    def backtrack(self, v, no_colors, colors):
        if self.no_v == v:
            return True
        for i in range(1, no_colors + 1):
            if self.valid_color(v, i, colors):
                colors[v] = i
                if self.backtrack(v + 1, no_colors, colors):
                    return True
        return False

    def valid_color(self, colored_vertex, vertex_color, colors):
        for i in range(self.no_v):
            if self.matrix[colored_vertex][i] == 1 and vertex_color == colors[i]:
                return False
        return True
