import pyautogui
import pyperclip
import webbrowser
import time
import yfinance
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.float_format = '{:.2f}'.format

acao = input("Digite o codigo da acao desejada: ")
inicio = input("Digite a data de inicio desejada (aaaa-mm-dd): ")
fim = input("Digite a data de fim desejada (aaaa-mm-dd): ")

df = yfinance.Ticker(acao).history(start=inicio, end=fim)

df= df.drop(["Dividends", "Stock Splits"], axis=1)

abertura = df.Open
fechamento = df.Close
maximo = df.High.max()
minimo = df.Low.min()

destinatario = "feliperoll07@gmail.com"
assunto = "Email de Teste"
mensagem = f"""
Isto eh um teste

Exibindo dados da acao {acao} com inicio em {inicio} e final em {fim}. O valor maximo neste perido eh de {maximo:.2f} e o minimo de {minimo:.2f}

Excluir este email
""" 

webbrowser.open("www.gmail.com")
time.sleep(5)

pyautogui.PAUSE = 3

pyautogui.click(x=-1251, y=338)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=-522, y=853)

print("Email enviado!")
