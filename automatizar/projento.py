import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minimo = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "guihcunha12@gmail.com"
assunto = "analise do projento"

#criar mensagem
mensagem = f"""
prezado gestor,

seguem as análises solicitadas da ação {ticker}:

cotação máxima: R${maxima}
cotação mínima: R${minimo}
valor médio: R${valor_medio}

Qualquer dúvida, estou à sua disposição !
"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(10)

#CONFIGURANDO UMA PAUSA
pyautogui.PAUSE = 5

#clicaar no botao escrever
pyautogui.click(x=75, y=180)

#digitar o email do destinatario e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#clicar no botao enviar
pyautogui.click(x=835, y=697)

#fechar o gmail
pyautogui.click("ctrl", "f4")

print("email enviado com sucesso!")
