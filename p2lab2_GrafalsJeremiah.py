current_price = int(input())
last_months_price = int(input())

price_change = current_price - last_months_price
mortgage = (current_price*.051)/12
print('This house is $',current_price,'. The change is $',price_change,' since last month.',sep='')
print('The estimated monthly mortgage is $',format(mortgage,'.2f'),'.',sep='')