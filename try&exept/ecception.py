a = int(input("first num: "))
b = int(input("second num: "))

try:
    result = int(a/b)
except ZeroDivisionError:
    print("bad math")
print("result: " + str(result))

result_2 = a + b
print(result_2)