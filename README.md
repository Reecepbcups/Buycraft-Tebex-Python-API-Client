# Buycraft-Tebex-Python-API-Client
BuyCraft Tebex API Client for Python 3.X
Example File found in Example.py

# How to use
 - To import the API into your project, use 'from BuycraftAPI import BuycraftAPI' with the BuycraftAPI.py in your same current working Dirrectory
 - Place you 40 Char long secret Key into the token.txt file on the first line. This will be saved to a variable and passed through the main class.
  - Then save the buycraft class  with the token inside as an arugment to a simpler variable (b = BuycraftAPI(buycraftToken))
  - Call apon any funtion in the API with b.FUNCTION_NAME(Arguments_if_any)
