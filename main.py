import pygame
import sys

# Pygame初期化
pygame.init()

# ウィンドウサイズ設定（幅, 高さ）
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Pygame World")

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 背景色（R, G, B）を黒に設定して塗りつぶす
    screen.fill((0, 0, 0))

    # 画面更新
    pygame.display.flip()
