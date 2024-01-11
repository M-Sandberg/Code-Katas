import pandas as pd 


"""



"""


df = pd.read_csv( './exchange_rates_gaps/riksbanken_exchange_rates.csv' )

print( df[df["currency"] == "USD"] )