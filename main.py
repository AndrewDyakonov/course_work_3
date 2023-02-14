import funktion as funk

operations = funk.create_ex_class()

for i in range(5):
    print(operations[i].beautiful_data(), operations[i].description)
    print(operations[i].from_, operations[i].description)
    print(operations[i].summa, operations[i].currency)
    print()