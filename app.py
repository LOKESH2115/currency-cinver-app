from currency_converter import currencyconverter

c=currencyconverter()

amount=input("enter the amount:")
from_currency= input("from currency:").upper()
to_currency+ input("to currency").upper()

result=c.convert(amount,from_currency,to_currency)

print(result)
