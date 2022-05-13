import random
import django


class Grid:
    def __init__(self):
        # tamanho
        self.height = 100
        self.width = 100

        # patterns
        self.glider_pattern = [[0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0]]
        self.glider_gun_pattern = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0]]

        # criaçao dos grids
        self.grid_model = [0] * self.height
        self.next_grid_model = [0] * self.height
        for i in range(self.height):
            self.grid_model[i] = [0] * self.width
            self.next_grid_model[i] = [1] * self.width

    def __str__(self):
        return str(self.grid_model)

    # aleatoriza um grid
    def randomize(self, grid):
        for i in range(0, self.height):
            for j in range(0, self.width):
                grid[i][j] = random.randint(0, 1)

    # verifica o grid inteiro
    def next_gen(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                cell = 0
                count = self.count_neighbors(self.grid_model, i, j)

                if self.grid_model[i][j] == 0:
                    if count == 3:
                        cell = 1
                elif self.grid_model[i][j] == 1:
                    if count == 2 or count == 3:
                        cell = 1
                self.next_grid_model[i][j] = cell

        temp = self.grid_model
        self.grid_model = self.next_grid_model
        self.next_grid_model = temp

    # conta as celulas vivas ao redor de uma
    def count_neighbors(self, grid, row, col):
        count = 0
        if row - 1 >= 0:
            count = count + grid[row - 1][col]
        if (row - 1 >= 0) and (col - 1 >= 0):
            count = count + grid[row - 1][col - 1]
        if (row - 1 >= 0) and (col + 1 < self.width):
            count = count + grid[row - 1][col + 1]
        if col - 1 >= 0:
            count = count + grid[row][col - 1]
        if col + 1 < self.width:
            count = count + grid[row][col + 1]
        if row + 1 < self.height:
            count = count + grid[row + 1][col]
        if (row + 1 < self.height) and (col - 1 >= 0):
            count = count + grid[row + 1][col - 1]
        if (row + 1 < self.height) and (col + 1 < self.width):
            count = count + grid[row + 1][col + 1]
        return count

    # carrega um pattern para o grid
    def load_pattern(self, pattern, x_offset=0, y_offset=0):
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.grid_model[i][j] = 0

        j = y_offset

        for row in pattern:
            i = x_offset
            for value in row:
                self.grid_model[i][j] = value
                i = i + 1
            j = j + 1

if __name__ == '__main__':
    pass