#! python3
# Assertion explanation by my brother chatty

def inverso(numero):
    assert numero != 0, "El número debe ser diferente de cero"
    return 1 / numero


for n in (0, 1, 2, 3, 4):
    try:
        print(inverso(n))
    except AssertionError as e:
        print(f"Error: {e}")

print('\n')

def test_inverso():
    assert inverso(4) == 0.25, "El inverso de 4 debería ser 0.25"
    assert inverso(1) == 1, "El inverso de 1 debería ser 1"
    assert inverso(-2) == -0.5, "El inverso de -2 debería ser -0.5"
    print("No hace nada, pq todo bien\n")
    assert inverso(5) == 100, "El inverso de 5 debería ser 0.2"
    # assert inverso(10) == 100, "El inverso de 10 debería ser 0.1"
    # if you wanted to keep all the AssertionErrors, you must create a list an put them all there

try:
    test_inverso()
except AssertionError as e:
    print(f"Error -> {e}")
