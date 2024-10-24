# Komparasi Operasi

# is dan is not

a = 5
b = 5

hasil = a is b
print(a, "is", b, " =", hasil)
print(hex(id(a)))
print(hex(id(b)))

hasil = a is not b
print(a, "is not", b, " =", hasil)
print(hex(id(a)))
print(hex(id(b)))
