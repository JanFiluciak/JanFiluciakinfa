Entry_price = float(input("Cena przed obnizka: "))
print("znizka to 15%")
final_price = Entry_price*0.85
discount = Entry_price - final_price
print(f'Cena po obnizce {round(final_price , 2)}, ile zaoszczedziles {round(discount,2)}')
