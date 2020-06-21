import pyautogui
import time


comentarios = ["Fuma nao po :c", "SINGARO DA CARSI!!!","Escrevi e fui trabalhar quem leu quer me dar","Singaro da carci meu amigo"]
time.sleep(5)

for i in range(1000):
    pyautogui.typewrite(comentarios[i%4])
    pyautogui.typewrite("\n")
    time.sleep(2)