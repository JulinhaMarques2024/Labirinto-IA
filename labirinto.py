
class Labirinto:
    """
    Classe que representa um labirinto com uma grade, posição inicial e objetivo.

    Attributes:
        grid (List[List[int]]): Matriz 2D representando o labirinto onde:
            0 representa parede
            1 representa caminho livre
        inicio (tuple): Tupla (x,y) representando a posição inicial
        objetivo (tuple): Tupla (x,y) representando a posição objetivo
    """
    def __init__(self, grid, inicio, objetivo):
        """
        Inicializa um novo labirinto.

        Args:
            grid (List[List[int]]): Matriz 2D do labirinto
            inicio (tuple): Posição inicial (x,y)
            objetivo (tuple): Posição objetivo (x,y)
        """
        self.grid = grid
        self.inicio = inicio
        self.objetivo = objetivo

    def vizinhos(self, posicao):
        """
        Encontra todos os vizinhos válidos de uma posição no labirinto.

        Args:
            posicao (tuple): Tupla (x,y) representando a posição atual

        Returns:
            List[tuple]: Lista de tuplas (x,y) representando as posições vizinhas válidas
        """
        x, y = posicao
        movimentos = [
            (-1, 0),  # Cima
            (1, 0),   # Baixo
            (0, -1),  # Esquerda
            (0, 1)    # Direita
        ]
        
        for dx, dy in movimentos:
            bx, by = x + dx, y + dy
            if 0 <= bx < len(self.grid) and 0 <= by < len(self.grid[0]) and self.grid[bx][by] != 0:
                yield (bx, by)
