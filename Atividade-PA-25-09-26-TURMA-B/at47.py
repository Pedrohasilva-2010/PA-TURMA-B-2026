popA = 80000
popB = 200000
anos = 0

while popA <= popB:
    popA = popA + (popA * 0.03)
    popB = popB + (popB * 0.015)
    anos = anos + 1

print(f"Em {anos} anos a Cidade A ultrapassa a Cidade B.")