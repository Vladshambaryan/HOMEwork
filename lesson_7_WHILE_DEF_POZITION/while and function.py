i = 0

while i < 5:  # пока i < 5
    print('hello')
    i += 1  # к тому что находится в i + 1

print('The end')


while True:
    user_input = input('Enter something: ')
    if user_input == 'exit':
        break  # break
    elif user_input == 'skip':
        print('skipping.....')
        continue  # прерывать текущий и последующий шаг
    elif len(user_input) > 10:
        print('Your input is too long')
    else:
        print('input is ok')

print('Good bye!')


