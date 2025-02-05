import pyautogui
import time

print("Posicione o mouse sobre o botão desejado. A posição será exibida a cada 2 segundos.")

while True:
    x, y = pyautogui.position()
    print(f"Posição atual do mouse: X={x}, Y={y}")
    time.sleep(5)  # A cada 2 segundos, ele atualiza a posição
