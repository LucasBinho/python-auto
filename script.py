import pyautogui
import time
import webbrowser

# 1. Abrir o navegador e acessar o Hotmail
webbrowser.open("https://outlook.live.com/mail/")  
time.sleep(5)  # Espera carregar

botao_img = pyautogui.locateOnScreen('email_btn.png', confidence=0.8)

# screenshot = pyautogui.screenshot()
# screenshot.save('screenshot.png')

if botao_img:
    pyautogui.click(botao_img)  # Clica na posição do botão
    print("Botão 'Novo e-mail' encontrado e clicado!")
else:
    print("Botão 'Novo e-mail' não encontrado na tela.")
time.sleep(3)

pyautogui.write("ti@wepando.com")
time.sleep(2)
pyautogui.press("enter")  
time.sleep(2)
pyautogui.press("tab")  

# 4. Digitar o assunto
pyautogui.write("Teste de Automacao")
time.sleep(2)
pyautogui.press("tab")  
time.sleep(2)

pyautogui.write("Ola VAPO TEAM, este e um email automatico. Nao foi o binho, repito, nao foi o binho. Foi o RoBinho")
time.sleep(2)


pyautogui.hotkey("ctrl", "enter")

print("E-mail enviado com sucesso!")
