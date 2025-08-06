# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

def solve_maze(maze):
    # Cria uma nova pilha
    stack = deque()
    
    # Localiza a posição inicial do jogador
    start_pos = maze.get_init_pos_player()
    stack.append(start_pos)
    
    # Conjunto para manter registro de posições visitadas
    visited = set()
    
    while stack:
        # Retira uma localização da pilha
        current_pos = stack.pop()
        
        # Verifica se encontrou o prêmio
        if maze.find_prize(current_pos):
            maze.mov_player(current_pos)
            print("Caminho encontrado!")
            return True
        
        # Se não for o prêmio e não foi visitado ainda
        if current_pos not in visited:
            visited.add(current_pos)
            maze.mov_player(current_pos)
            time.sleep(0.05)  # Pequena pausa para visualização
            
            # Verifica posições adjacentes
            x, y = current_pos
            adjacent_positions = [
                (x-1, y),  # cima
                (x+1, y),  # baixo
                (x, y-1),  # esquerda
                (x, y+1)   # direita
            ]
            
            # Insere posições válidas na pilha
            for pos in adjacent_positions:
                if (0 <= pos[0] < maze.M.shape[0] and 
                    0 <= pos[1] < maze.M.shape[1] and 
                    maze.is_free(pos) and 
                    pos not in visited):
                    stack.append(pos)
    
    print("Caminho não encontrado!")
    return False

# Carrega e exibe o labirinto
maze_csv_path = "labirinto1.txt"
maze = Maze() 
maze.load_from_csv(maze_csv_path)
maze.run()

# Inicializa jogador e prêmio
maze.init_player()

# Resolve o labirinto
solve_maze(maze)

# Mantém a janela aberta
while True:
    time.sleep(1)