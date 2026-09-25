n = int(input("Quantos elementos mostrar? "))
t1 = 0
t2 = 1

if n >= 1:
    print(t1, end="")
if n >= 2:
    print(f", {t2}", end="")

for i in range(2, n):
    t3 = t1 + t2
    print(f", {t3}", end="")
    t1 = t2
    t2 = t3
print()