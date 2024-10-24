# python - m py_compile Main.py

from ctypes import c_double
print("Hello World")

data_ingteger = "1.4"
print("Data : ", data_ingteger, "Betipe : ", type(data_ingteger))

data_complex = complex(5, 6)
print("Data : ", data_complex, "Betipe : ", type(data_complex))

data_double = c_double(10.5)
print("Data : ", data_double, "Betipe : ", type(data_double))
