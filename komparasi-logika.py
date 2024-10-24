inputUser = float(input("Masukan angka kurang dari 3 atau lebih dari 10:"))

isKurangDari = inputUser < 3
isLebihDari = inputUser > 10

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan: ", isCorrect)

inputUser = float(input("Masukan angka kurang dari 3 atau lebih dari 10:"))

isDiantara = inputUser > 3 and inputUser < 10
print("Angka yang anda masukan: ", isDiantara)

inputUser = float(input("Masukan angka 0-5 atau 8-11: "))

isOne = inputUser > 0 and inputUser < 5 or inputUser > 8 and inputUser < 11
print("Angka yang anda masukan: ", isOne)

inputUser = float(
    input("Masukan angka kurang dari 0 atau 5-8 atau lebih dari 11: "))
isTwo = inputUser < 0 or inputUser > 5 and inputUser < 8 or inputUser > 11
print("Angka yang anda masukan: ", isTwo)
