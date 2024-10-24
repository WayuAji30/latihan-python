a = 9
b = 8

c = a | b
print("=====OR======")
print("Angka:", a, ", Binary:", format(a, "08b"))
print("Angka:", b, ", Binary:", format(b, "08b"))
print("Angka:", c, ", Binary:", format(c, "08b"))

c = a & b
print("=====AND======")
print("Angka:", a, ", Binary:", format(a, "08b"))
print("Angka:", b, ", Binary:", format(b, "08b"))
print("Angka:", c, ", Binary:", format(c, "08b"))

c = a ^ b
print("=====XOR======")
print("Angka:", a, ", Binary:", format(a, "08b"))
print("Angka:", b, ", Binary:", format(b, "08b"))
print("Angka:", c, ", Binary:", format(c, "08b"))

c = ~a
print("=====NOT======")
print("Angka:", a, ", Binary:", format(a, "08b"))
print("Angka:", c, ", Binary:", format(c, "08b"))
d = 0b00000000
e = 0b11111111
print("Angka:", e ^ d, "Binary:", format(e ^ d, "08b"))

c = a >> 2
print("=====RIGHT SHIFT======")
print("Angka:", a, ", Binary:", format(a, "08b"))
print("Angka:", c, ", Binary:", format(c, "08b"))

c = a << 2
print("=====LEFT SHIFT======")
print("Angka:", a, ", Binary:", format(a, "08b"))
print("Angka:", c, ", Binary:", format(c, "08b"))
