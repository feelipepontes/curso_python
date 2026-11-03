# Exercício 021 - Reproduzindo um arquivo MP3
# Carrega e reproduz um arquivo de áudio utilizando a biblioteca pygame.

# Importa as bibliotecas pygame e time.
import pygame
import time

# Inicializa os módulos da biblioteca pygame.
pygame.init()

# Carrega o arquivo MP3 para reprodução.
pygame.mixer.music.load('ex021.mp3')

# Inicia a reprodução do áudio carregado.
pygame.mixer.music.play()

# Mantém o programa em execução por 60 segundos.
time.sleep(60)






