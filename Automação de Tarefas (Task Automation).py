#!/usr/bin/env python
# coding: utf-8

# # Passo a passo do Problema (Step-by-Step Problem Solving)
# - Passo 1 - Buscar datas das ações automaticamente (Step 1 - Fetch stock data automatically)
# - Passo 2 - Realizar as análises solicitadas pelo gestor (Step 2 - Perform the requested data analysis)
# - Passo 3 - Enviar automaticamente um e-mail com o resultado da análise (Step 3 - Send automatically an e-mail containing the data analysis result)

# # Passo 1 (Step 1) - Buscar datas das ações automaticamente (Fetch stock data automatically)

# In[2]:


get_ipython().system('pip install yfinance')


# In[75]:


import yfinance as yf

Ticker = input("Digite o código da ação: ")
dados = yf.Ticker(Ticker).history("6mo")
fechamento = dados.Close
fechamento.plot()


# # Passo 2 (Step 2) - Realizar as análises solicitadas pelo gestor (Perform the requested data analysis)
# - Cotação Máxima (High)
# - Cotação Mínima (Low)
# - Cotação Atual  (Current)

# In[76]:


maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
atual = round(fechamento[-1],2)

print(maxima)
print(minima)
print(atual)


# # Passo 3 (Step 3) - Enviar automaticamente um e-mail com o resultado da análise (Realizar as análises solicitadas pelo gestor (Perform the requested data analysis)
# 
# - abrir uma nova aba (ctrl + t) (open a new tab)
# - digitar www.gmail.com e dar um enter (type www.gmail.com e hit enter)
# - clicar no botão escrever (click on the "write" button)
# - digitar o destinatário (tab) (type the recipient)
# - digitar o assunto (tab) (type the subject)
# - preencher o corpo do e-mail (fill in the body with the message)
# - clicar no botar enviar (click on the "send" button)

# In[34]:


get_ipython().system('pip install pyautogui')


# In[36]:


get_ipython().system('pip install pyperclip')


# In[47]:


import pyautogui
import pyperclip


# In[81]:


# dar uma pausa de 5 segundos entre os passos (5 seconds interval between actions)
pyautogui.PAUSE = 5

# abrir uma nova aba (ctrl +t) digitar www.gmail.com e dar um enter
pyautogui.hotkey("ctrl", "t")

#digitar www.gmail.com e dar um enter (type www.gmail.com e hit enter)
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

#clicar no botão escrever (click on the "write" button)
pyautogui.click(x=75, y=212)

#digitar o destinatário (tab) (type the recipient)
pyperclip.copy("josetoffoli@hotmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#digitar o assunto (tab) (type the subject)
pyperclip.copy("Análises Diárias")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#preencher o corpo do e-mail (fill in the body with the message)
mensagem = f"""
Prezado Gestor,

Seguem, conforme solicitadas, as análises dos últimos seis meses da ação {Ticker}:

Cotação máxima: {maxima}
Cotação mínima: {minima}
Cotação atual: {atual}

Qualquer dúvida, fico à disposição para o esclarecimento de quaisquer dúvidas.

Atte.
Vitor Hugo Toffoli
"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#clicar no botar enviar (click on the "send" button)
pyautogui.click(x=1197, y=991)
print("email enviado com sucesso!")


# In[ ]:




