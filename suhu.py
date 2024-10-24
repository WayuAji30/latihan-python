# latihan konversi suhu

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam satuan celcius:'))
print('suhu dalam celcius: ', celcius)

reamur = (4/5) * celcius
print('suhu dalam reamur: ', reamur)

fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit: ', fahrenheit)

kelvin = celcius + 273
print('suhu dalam kelvin: ', kelvin)


print("\nPROGRAM KONVERSI TEMPERATUR FAHRENHEIT\n")

fahrenheit = float(input('Masukan suhu dalam satuan fahrenheit:'))
print('suhu dalam fahrenheit: ', fahrenheit)

celcius = 5/9 * (fahrenheit-32)
print('suhu dalam celcius: ', celcius)

reamur = 4/9 * (fahrenheit-32)
print('suhu dalam reamur: ', reamur)

kelvin = 5/9 * (fahrenheit-32) + 273
print('suhu dalam kelvin: ', kelvin)


print("\nPROGRAM KONVERSI TEMPERATUR KELVIN\n")

kelvin = float(input('Masukan suhu dalam satuan kelvin:'))
print('suhu dalam kelvin: ', kelvin)

celcius = kelvin - 273
print('suhu dalam celcius: ', celcius)

reamur = 4/5 * (kelvin-273)
print('suhu dalam reamur: ', reamur)

fahrenheit = 9/5 * (kelvin-273) + 32
print('suhu dalam kelvin: ', fahrenheit)
