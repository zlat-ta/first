responses = {}

# установка флага продолжения опроса
polling_active = True

while polling_active:
    #запрос имени и ответа пользователя
    name = input("\nКак тебя зовут? ")
    response = input("На какую гору вы хотели бы взобраться?")

    #ответ сохраняется в словаре
    responses[name] = response

    #проверка продолжения опроса
    repeat = input("Хотели бы вы, чтобы ответил другой человек? (yes / no) ")
    if repeat == 'no':
        polling_active = False

#опрос завершен, вывести результат
print("\n--- Все результаты ---")
for name, response in responses.items():
    print(f"{name} хотел бы взобраться на {response}.")