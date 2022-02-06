import pyautogui

num = int(input("Wprowadź liczbę do podzielenia od 100"))
if num == 0:
   pyautogui.alert("Uwaga! Nie można dzielić przez 0")
else:
    print(f'Wynik to: {100/num}')