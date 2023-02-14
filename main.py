import funktion as funk

operations = funk.create_ex_class()

for operation in operations:
    print(operation.beautiful_data(), operation.description)
    print(f'{operation.from_}  ->  {operation.to}')
    print(operation.summa, operation.currency)
    print()
