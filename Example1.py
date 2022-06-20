##code1

list = ['Buzdanov Andrian']
fio = (input("Введи:"))
check = list
if fio in check[0]:
    print(f'{fio} Введеные данные найдены в списке {list}')
else:
    print(f'Введенный вами пользователь {fio} не найден  в строке {list}')

##code2
vlan = [10, 20, 30, 40]
vlan_id_input = input("Введи Vlan: ")
if vlan_id_input.isdigit():
    vlan_int = int(vlan_id_input)
    print(f"Введеный vlan: {vlan_id_input}, преобразован в (int):{vlan_int}")
if vlan_id_input in vlan:
    print(f'Введенный вами vlan:"{vlan_id_input}",\n, Был найден в списке vlanov "{vlan}"')
elif vlan != 0:
    print(f'В списке есть объекты {vlan}')
else:
    print('Список пуст')
if vlan_int not in vlan:
    vlan.append(vlan_int)
    print(f'VLAN {vlan_id_input} не было в списке, он был добавлен в него {vlan}')
else:
    print(f'VLAN {vlan_int} уже содержится в списке {vlan}')

##code3
import re
def validate():
    while True:
        login = input('Введите пользователя:')
        password = input("Enter a password:")
        if len(password) < 16:
            print("Убедитесь, что ваш пароль состоит как минимум из 16 букв")
        elif re.search('[login]', password) is None:
            print('Пароль содержит имя пользователя')
        elif re.search('[0-9]', password) is None:
            print("Убедитесь, что в вашем пароле есть цифры")
        elif re.search('[A-Z]', password) is None:
            print("Убедитесь, что в вашем пароле есть заглавная буква")
        elif re.search('[a-z]', password) is None:
            print("Убедитесь, что в вашем пароле есть строчные буквы")
        else:
            print(f'Пароль для пользователя "{login}" установлен')
        break
validate()

