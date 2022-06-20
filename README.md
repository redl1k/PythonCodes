# PythonCodes                  
Маленькиe программы написанные для себя, которые выполняют какие либо функции. Описал ниже, что за функции:

##Example1##
Здесь я собрал 3 программы, которые выполняют следующие функции:
                                          
                                          
==code1                                                                                    
И за переменный я взял свою фамилию и имя                                                                                       
1.При вводе с клавиатуры фамилии выводится сообщение: пользователь {фамилия и имя} найден.                                          
2.При выводе фамилия и имя должны браться из заранее созданного списка (list).                                                               
3.При вводе любого другого значения пусть выводится сообщение: пользователь {то что вводилось с клавиатуры} не найден.                     
                                          
==code2
Реализованна программа, которая проверяет содержится ли в списке с VLAN ID вводимый с клавиатуры VLAN.                                          
1.Определит список с VLAN ID содержащий элементы в виде целых чисел (int).                                          
Реализован ввод с клавиатуры VLAN ID и добавления его к созданному списку, при этом опишит проверку следующих условий:                     
                                          
-Если список VLAN пуст:                                          
Выведет сообщение о том, что список был пуст                                          
Добавит введеный VLAN ID в список                                          
Выведет сообщение о добавлении VLAN ID и сам список                                          
                                          
-Если список VLAN не пуст, но введённого VLAN ID в списке нет:                                                                                    
Выведет сообщение о том, какие VLAN содержал список                                                                                    
Добавит введённый VLAN ID в список                                                                                    
Выведет сообщение о добавленнии VLAN ID и сам список                                                                                    
                                          
-Если введённый VLAN ID уже содержится в списке:                                          
--Выведет сообщение о том, что такой VLAN ID уже содержится в спике                                          
--Выведет список VLAN                                          
                                          
==code3                                          
Реализована программа проверяющая пароль на удовлетворение следующим условиям:                                          
● Логин – строка присвоенная переменной и содержащая фамилию                                          
● Пароль вводите с клавиатуры и присваиваете другой переменной                                          
● Введённый пароль должен быть длиннее 16 символов                                          
     – если пароль короче должно выводится соответствующее сообщение                                          
                                               
● Введённый пароль не должен содержать имя пользователя                                          
● Пароль должен содержать цифры                                          
● Пароль должен содержать строчный буквы                                          
● Пароль должен содержать заглавные буквы                                          
     – в противном случае должно выводится соответствующее сообщение                                          
                                          
● Если все условия пройдены успешно, то выводится сообщение:                                          
«Пароль для пользователя {ваш логин} задан                                          
