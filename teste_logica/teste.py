from grid_ob import Grid
from PIL import Image


def draw(row, col, color='black'):
    # tamanhoem px de uma celula
    cell_size = 5

    # define o outline de uma celula
    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'


def img(grid: list):
    # apagar a visualizção
    # usar o metodo next_gen()
    # iterar o grid e se for 1 desenhe uma célula
    # enquanto estiver rodadando chama ela mesmo
    for i in range(0, grid.height):
        for j in range(0, grid.width):
            if grid.grid_model[i][j] == 1:
                pass
    # salva em um arquivo para a visualizção
    # im = Image.fromarray(img_test)
    # im.save("filename.jpeg")


if __name__ == '__main__':
    grid = Grid()
    grid.load_pattern(grid.glider_pattern)
    img(grid)
