"""This module shows the use of continue and break in both types of loops"""


def test_while_loop():
    secret = 'swordfish'
    pw = ' '
    auth = False
    count = 0
    max_attempt = 5

    while pw != secret:
        count += 1
        if count == max_attempt: break
        if count == 3: continue
        pw = input(f"{count}: Whats's the secret word? ")
    else:
        auth = True
    print("Authorized" if auth else "Calling the FBI....")


def test_for_loop():
    animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

    for pet in animals:
        if pet =='bear': continue
        if pet == 'cat': break
        print(pet)
    else:
        print("All the animals")


test_while_loop()
test_for_loop()