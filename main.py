# a = range(-5,5)
# a = [-3,-2,-1,0,1,2,3,4,5,6]
# print(a[::-1])
#
# s='hello kitty'
# p=s.split()
# print(p[::-1])
# print(p[:2])
#
# a="order1"
# b="order2"
# c="order3"
# orders=[]
# orders.append(a)
# orders.append(b)
# orders.append(c)
# print(orders)
#
#
#
# book1="my book"
# book2="your book"
# books=["all_books"]
# books.append(book1)
# books.append(book2)
# print(books)
#
# my_books=['book1','book2','book3','book4','book5']
# tom_books=my_books.copy()
# print(my_books,tom_books)
#
#
# my_bookss=['book1','book2','book3','book4','book5']
# my_orders=['order1','order2','order3','order4','order5']
#
# all_things=['order1','order2','order3']
# only_books=['book1','book2']
# all_things.extend(only_books)
# print(all_things)
#
#
# nums=[1,2,3,4,5,6,7,8,9,10]
# print(nums)
# nums.reverse()
# print(nums)
#
#
# random_values = [3, 5, 0, -1, 2, 10, 15, -5]
# random_values.sort()
# print(random_values)
#
#
# a = (1,2,3,4,5,6)
# # создадим кортеж
# b = [1,2,3,4,5,6]
# # создадим список с теми же элементами, что в кортеже выше
# print(a.__sizeof__())
# # 36
# print(b.__sizeof__())
# # 44
#
# tpl2=(255,)
# print(tpl2)
#
#
# place_and_money = {1: 100, 2: 50, 3: 10}
# #place_and_money[3]=25
# place_and_money.setdefault(10,1)
#
# #place_and_money.pop(3)
# print(place_and_money)
#
#
#
# name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
# print(name_to_age.keys())
# print(name_to_age.values())
# name_to_age.update({'Anne':23,'Phillip':29})
# print(name_to_age)
#
#
#
#
# name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
#
# print(name_to_age)
#
# test_dict={}
# test_dict.setdefault(5,[3,4,5])
# print(test_dict)
# test_dict.setdefault((3,4,5),'strong man')
# print(test_dict)
#
# #Создайте пустой словарь test_dict2. По ключу 'name' поставьте строку 'Sancho'. В качестве значения для ключа 'surname' поставьте 'Panso'. А для ключа 'info' добавьте словарь {'age': 35, 'country': 'Mexico'}.
# test_dict2={}
# test_dict2.__setitem__('name','Sancho')
# test_dict2.__setitem__('surname','Panso')
# test_dict2.__setitem__('info',{'age': 35, 'country': 'Mexico'})
# test_list3=[]
# test_list3.append(test_dict2)
# print(test_dict2)
# print("===")
# test_dict3={}
# test_dict3.__setitem__('info',[10, 15, 27])
# test_dict3.__setitem__('about','dont know')
# print(test_dict3)
# test_dict3.update({'about':{'game': 'football', 'period': 5}})
# print(test_dict3)
#
# s2= {5,10,3,2,11}
# print(s2)
# s3=set("wow thats cool")
# print(s3)
#
# s1=set("abcde")
# s1.add("hello")
# print(s1)
#
# s1=set("abcdef")
# s1.remove('f')
# print(s1)
#
# alpha_set=set("abcde")
# name=set("bad boy")
# print(alpha_set)
# print(name)
# print(alpha_set.union(name))
#
#
# num_set=set([1,2,3,4,5,6,7,8,9,10,0])
# date_num=set([1,9,4,8])
# print(date_num)
# print(num_set.union(date_num))
#
#
# alpha_set=set("abcde")
# name=set("bad boy")
# print(alpha_set)
# print(name)
# print(alpha_set.intersection(name))
#
# num_set=set([1,2,3,4,5,6,7,8,9,10,0])
# date_num=set([1,9,4,8])
# print(date_num)
# print(num_set.intersection(date_num))
#
#
# num_set=set([1,2,3,4,5,6,7,8,9,10,0])
# date_num=set([1,9,4,8])
# print(date_num)
# print(num_set.difference(date_num))
#
# alpha_set=set("abcde")
# name=set("bad boy")
# print(alpha_set)
# print(name)
# print(alpha_set.difference(name))
#
#
# alpha_set=set("abcde oy")
# name=set("bad boy")
# print(alpha_set)
# print(name)
# print(name.issubset(alpha_set))
#
#
# a=float(3)
# b=3.5
# c=a+b
# print(c)
#
# list1=[1,2,3,4,5]
# #list1=list()
# tpl1=tuple(list1)
# print(list1)
# print(tpl1)
#
# tpl2=("abcde")
# print(tpl2)
# list2=list(tpl2)
# print(list2)
#
# list2=list()
# l=range(-5,15,2)
# print(list(l))
# list3=[1,2,3,4]
# list3.extend(l)
# print(list3)
#
# list2 = range(-5, 15, 2)
# list3 = [1, 2, 3, 4]
# list3.extend(list2)
# print(list3)
#
#
# list6=[3, 1, -10, 5, 11, 20, 1, -10]
# list7=list6.copy()
# list6.sort()
# list6.reverse()
# print(list6)
# print(list7)
# list_result=list6.copy()
# print(list_result)
#
# list1=[10,15]
# tpl1=tuple(list1)
# dict1={}
# dict1.update({tpl1:'hello'})
# print(dict1)
#
# dict1={'name':'unknown'}
# dict2={'name':'Tom'}
# dict2=dict(name='Tom')
# print(dict1,dict2,dict1.keys(),dict1.values())
#
# s1=set("hello")
# s2=['w','o','w']
# print(s1)
# print(s2)
# print(s1.union(s2),s1.difference(s2),s1.intersection(s2))
#
#
# print(not True and not False and True or False)
# print(not False and True or False and not True)
# #======
# def square(nn):
#     return nn ** 2
#
# num=[1, 2, 3, 4, 5]
# sqrd=map(square,num)
# print(list(sqrd))
# #======
# num=[1, 2, 3, 4, 5]
# sqrd=map(lambda nn:nn**2,num)
# print(list(sqrd))
# #======
# #https://pythonru.com/osnovy/vse-chto-nuzhno-znat-o-lambda-funkcijah-v-python
#
# N=range(1,30,1)
# print(list(N))
# print(list(map(lambda x:x in range(1,30,1),[31,7])))
#
# print(list(N))
# print(list(map(lambda x:x in range(1,30,1),[31,7])))
#
#
#
# print(list(str(123456789)))
# print(list(map(int,list(str(123456789)))))
#
#
#
# print(list(map(int,list(str(123123123)))))
#
# print(list(map(lambda x:x in "123456789",['3','7'])))
# print("========")
# print()
# print(list(map(lambda x:True if x % 2 == 0 else False,[4])))
#
#
# try:
#     #a=int(input("234"))
#     #print(a)
#     print("ok")
# except:
#     print("нет")
# finally:
#     print("Exit")
#
#
# def are_both_odd(A, B):
#     return (A % 2 != 0 and B % 2 != 0)
#
# print(are_both_odd(2, 3))
#
#
# x=-1
# y=-1
# if x > 0:
#     if y > 0:               # x > 0, y > 0
#         print("First quarter") # Первая четверть
#     else:                   # x > 0, y < 0
#         print("Fourth quarter") # Четвёртая четверть
# else:
#     if y > 0:               # x < 0, y > 0
#         print("Second quarter") # Вторая четверть
#     else:                   # x < 0, y < 0
#         print("Third quarter") # Третья четверть
#
# if x>0 and y>0:
#     print("First quarter")
# if x<0 and y>0:
#     print("Second quarter")
# if x>0 and y<0:
#     print("Fourth quarter")
# if x<0 and y<0:
#     print("Third quarter")
# mounth=2
# if mounth in [3,4,5]:
#     print("Spring")
# elif mounth in [6,7,8]:
#     print("Summer")
# elif mounth in [9,10,11]:
#     print("Autumm")
# elif mounth in [12,1,2]:
#     print("Winter")
# else: print("Это не месяц")
#
#
# def get_wind_class(speed):  # Объявление функции
#     if 1<=speed<=4:
#         s="weak [1]"
#     if 5<=speed<=10:
#         s="moderate [2]"
#     if 11<=speed<=18:
#         s="strong [3]"
#     if speed>=19:
#         s="hurricane [4]"
#     return s
# print(get_wind_class(3))
#
#
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# print(user_database["user"])
# def check_user(username, password):
#     if username in user_database.keys():
#         if password == user_database[username]:
#             return True
#         else: return False
#     else:
#         return False
# print(check_user("use2r",'password'))
#
# a=53
# b=33
# c=53
# i=0
#
# if a<45:
#     i=1
# if b<45:
#     i+=1
# if c<45:
#     i+=1
# if i==1:
#     print("True")
#
# a=1
# if not ((a in range(-10,-1,1)) or (a in range(2,15,1))):
#     print("nono")
# c=30
# print(c//5)
# print(c%5)
# print(c//5%2)
# #ЗАДАНИЕ 5.7
# if (c%5==0 and c//5>=2 and (c//5)%2!=0) or (c==50):
#     print("ok")
#
#
# print("========")
# ll=[1,2,2,1,1,3]
# ll2=[1,2,3]
# n=list()
# n=[1,1,2,1,1]
# print(n)
# llout11=set(n)
# print(llout11)
#
# lst = [98, 24, 23, 12, 3]
# s=1
# for i in lst:
#     print(i)
#     s*=i
# print(s)
# n=10
# for i in range(1,n+1):
#     print("*"*i)
#     print(i)
#
# my_list = [1]
# for i in range(10):
#     my_list.append(my_list[i] * 2)
#     print(i)
# print(len(my_list))
# print(my_list)
#
# word_list = ['My', 'name', 'is', 'Sergei']
# s=""
# for i in word_list:
#     s+=i
#     s+=" "
# print(s)
#
#
# num_list = [1, 10, 3, -5]
# num_list.sort()
# print(num_list)
#
# my_list = list(range(0, 100, 3))
# d=0
# for i in my_list:
#     if i%2==0:
#         d+=1
# print(d)
#
# my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
# for i in my_list:
#     if type(i)==str:
#         print(i)
#
# l=3.3
# t=0
# while t<10:
#    t+=l
# print(t-10)
#
# t=0
# n=0
# while n<500:
#     t+= 1
#     n+=t
#
# print(n)
# print(t)
#
# S = 0  # создаём накопительную переменную, в которой будем считать сумму
# n = 1  # задаём текущее натуральное число
#
# # создаём цикл, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай, пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # увеличиваем значение натурального числа
#     #print("Still counting ...")  # выводим строку ожидания
# print()  # отделяем промежуточный вывод от результата пустой строкой
# print("Sum is: ", S)  # выводим результирующую сумму
# print("Numbers total: ", n - 1)  # выводим результирующее количество чисел
#
#
# t=1
#
# while l<1000:
#     t += 1
#     l=t
#     l=t**2
#
# print(t-1)
# print(31**2)
#
# t=0
# while True:
#     if (t**2 > 1000):
#         break
#     t += 1
# print(t)
#
#
# t=0
# l=1
# while True:
#     if 3**t>1000:
#         break
#     t+=1
# print(t)
# print(3**6)
#
#
# t=1000
# p=0.08
# n=0
# while t<3000:
#     t=t+0.08*t
#     n+=1
# print(n)
# print(t)
#
#
#
# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# number_negative = None #объявляем переменную, в которой будем хранить номер последнего дня оттока, изначально она пустая (None)
# N = len(user_dynamics) #вычисляем длину списка
# #создаём цикл по элементам последовательности от 0 до N (не включая N)
# for i,usrd in enumerate(user_dynamics): # i — индекс текущего элемента
#     #проверяем условие оттока — текущий элемент отрицательный
#     if usrd < 0: #если условие истинно,
#         print("Churn value: ", usrd) # выводим количество ушедших в этот день пользователей
#         print("Number day: ", i+1) # выводим номер дня
#
#
# my_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
# i=0
# for ttest in my_dict.values():
#     #print(type(ttest),"   --   ",ttest)
#     if type(ttest) is str:
#         print(type(ttest),"   --   ",ttest)
#         continue
#     else:
#         i+=1
# print(i)
#
# text = """
# The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.
#
# Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.
#
# `Well!' thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)
# """
# text = text.lower()  # приводим текст к нижнему регистру
# text = text.replace(" ", "")  # заменяем пробелы на пустые строки
# text = text.replace("\n", "")  # заменяем символы переноса строки на пустые строки
# count_dict = {}  # создаём пустой словарь для подсчёта количества символов
# # создаём цикл по символам в строке text
# for symbol in text:  # symbol — текущий символ в тексте
#     # проверяем условие, что символа ещё нет среди ключей словаря
#     if symbol not in count_dict:  # если условие выполняется,
#         count_dict[symbol] = 1  # заносим символ в словарь со значением 1
#     else:  # в противном случае
#         count_dict[symbol] += 1  # увеличиваем частоту символа
# print(count_dict)  # выводим результирующий словарь
#
#
#
# text = """
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I am sure.
# So if she sells sea shells on the sea shore,
# I am sure that the shells are sea shore shells.
# """
# text = text.lower() #приводим текст к нижнему регистру
# text = text.replace("\n", " ") #заменяем символы переноса строки на пробелы
# text = text.replace(",", "") #заменяем запятые на пустые строки
# text = text.replace(".", "") #заменяем точки на пустые строки
# text = text.replace(";", "") #заменяем точки с запятыми на пустые строки
# word_list = text.split()
# count_dict = {} #создаём пустой словарь для подсчёта количества слов
# #создаём цикл по словам в списке word_list
# for word in word_list: #word — текущее слово из списка word_list
#     #проверяем условие, что слова ещё нет среди ключей словаря
#     if word not in count_dict: #если условие выполняется,
#         count_dict[word] = 1 #заносим слово в словарь со значением 1
#     else: #в противном случае
#         count_dict[word] += 1 #увеличиваем частоту слова
# print(count_dict) #выводим результирующий словарь
#
#
# import random
# my_list = []
# for i in range(0, 10):
#     my_list.append(random.randint(0, 10))
# for i in range(0, 10):
#     if my_list.count(i)>1:
#         print(i," yes")
# print(my_list)
# n=0
# for i in my_list:
#     if n>=10:
#         break
#     else:
#         n+=i
# print(n)
#
#
#
# attack = 80
# current_health=500
# seconds_num=0
# while True:
#     seconds_num+=1
#     current_health-=attack
#     if current_health<=0:
#         break
# print(seconds_num)
#
# attack = 80
# current_health=500
# seconds_num=0
# while current_health>0:
#     seconds_num+=1
#     current_health-=attack
# print(seconds_num)
#
#
# str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'knitting']
#
# cut_str_list = []
#
# for i, zp in enumerate(str_list):
#     cut_str_list.append({i:zp[:3]})
#
# print(cut_str_list)
#
#
# sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm'
# sentence=sentence.lower()
# sentence=sentence.replace(",","")
# list_sent=sentence.split(" ")
# print(list_sent)
# word_dict={}
# for sst in list_sent:
#     if sst not in word_dict:
#         word_dict[sst]=1
#     else:
#         word_dict[sst]+=1
# print(word_dict)
#
#
#
# str_list = ['text', 'morning', 'notepad', 'television', 'ornament','tttt']
# word_dict={}
# for st in str_list:
#     word_dict[st]=st.count("t")
# print(word_dict)
#
#
# def get_time(distance, speed):
#     # Если расстояние или скорость отрицательные, то возвращаем ошибку
#     if distance < 0 or speed < 0:
#         # Оператор raise возвращает (raise — досл. англ. "поднимать")
#         # объект-исключение. В данном случае ValueError (некорректное значение).
#         # Дополнительно в скобках после слова ValueError пишем текст сообщения
#         # об ошибке, чтобы сразу было понятно, чем вызвана ошибка.
#         raise ValueError("Distance or speed cannot be below 0!")
#     if speed ==0:
#         raise  ValueError("Distance or speed cannot be eq 0!")
#     result = distance / speed
#     return result
# print(get_time(100,1))
#
#
# def add_mark(name, mark, journal=None):
#     # Добавьте здесь проверку аргумента mark
#     mmt=(2,3,4,5)
#     if mark not in mmt:
#         raise ValueError("Huinya!")
#     if journal is None:
#         journal = {}
#     journal[name] = mark
#     return journal
#
# print(add_mark('ewqw',2))
#
# print("Shopping list:", end=' ')
# print("bread", "butter", "eggs",sep=",")
#
#
# def mult(*args):
#     # Вместо pass напишите тело функции
#     result = 1
#     for i in args:
#         result*=i
#         #print(t)
#     return result
# print(mult(3,5,10))
#
#
# def mean_mark(name, *marks):
#     result = sum(marks) / len(marks)
#     # Не возвращаем результат, а печатаем его
#     print(name + ':', result)
#
# mean_mark("Ivanov", 5, 5, 5, 4)
# mean_mark("Petrov", 5, 3, 5, 4)
#
#
# def get_length(name):
#     return len(name)
# new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
# #print(get_length(new_list))
# new_list.sort(key=get_length)
# #new_list.sort(key=lambda name: len(name))
# print(new_list)
#
#
# hyp = lambda a,b: (a**2+b**2)**(1/2)
# print(hyp(3,4))
# print(hyp(1,9))
#
#
# print("=="*20)
# t=[3,4,2,10]
# a = [1,2,3]
# a.sort()
# print(a)
#
# numbers_list = [3.4, 5.1, 2.2, 4.1, 1.0, 3.8]
# print(f'Before sorting: {numbers_list}')
# numbers_list.sort()
# print(f'After sorting: {numbers_list}')
#
#
# def sort_sides(l_in):
#     return l_in.sort()
# my_list=[(3, 4), (1, 2), (10, 10)]
# sort_sides(my_list)
# print(my_list)
#
#
#
# date="31012019"
# #print(split_date("31012019"))
# print(date[:2],date[2:4],date[4:],sep=".")
#
#
# def is_prime(n):
#     d = 2
#     if n<=1:
#         return False
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(13))
#
# def between_min_max(*nums):
#     min=nums[0]
#     max=nums[0]
#     for num in nums:
#         if num>max:
#             max=num
#         if num<min:
#             min=num
#     return (max + min)/2
#
# print(between_min_max(10))
# print(between_min_max(1,2,3,4,5))
#
#
# def best_student(**raiting):
#     min=100000
#     rr=""
#     for rait in raiting.keys():
#         if min>raiting[rait]:
#             min=raiting[rait]
#             rr=rait
#         #print(rait,raiting[rait])
#     return rr
# print("="*10)
# print(best_student(Tom=12, Mike=3))
# print(best_student(Tom=12))
# print(best_student(Tom=12, Jerry=1, Jane=2))
#
#
#
# is_palindrom = lambda a: "yes" if a==a[::-1] else "no"
# print(is_palindrom("qwq"))
#
#
# area = lambda a,b: a*b
# print(area(12,5))
#
#
# # 7.15
# between_min_max=lambda *rr:(sorted(rr)[0]+sorted(rr)[len(rr)-1])/2
# print(between_min_max(1,2,3,4,5))
#
#
# def sort_ignore_case(ls):
#     sorted_list = sorted(ls, key=str.casefold)
#     return sorted_list
# print(sort_ignore_case(['Acc', 'abc']))
#
#
# def exchange(usd=None, rub=None, rate=None):
#     k=0
#     if usd:
#         k+=1
#     if rub:
#         k+=1
#     if rate:
#         k+=1
#     if k>2:
#         raise ValueError('Too many arguments')
#     if k<2:
#         raise ValueError('Not enough arguments')
#     if rub and usd:
#         return rub/usd
#     if rub and rate:
#         return rub/rate
#     if usd and rate:
#         return usd*rate
#     return "123"
#
# print(exchange(usd=100, rub=8500))
# print(exchange(usd=100, rate=85))
# print(exchange(rub=1000, rate=85))
#
# global_counter = 0
#
#
# def add_one():
#     # Обозначим, что переменная global_counter
#     # является глобальной
#     global global_counter
#     global_counter += 1
#
#
# add_one()
# print(global_counter)
#
#
# def outer_function():
#     enclosing_counter = 0
#
#     def inner_function():
#         # С помощью оператора nonlocal покажем,
#         # что переменная enclosing_counter находится
#         # во внешней функции
#         nonlocal enclosing_counter
#         enclosing_counter += 1
#         print(enclosing_counter)
#
#     inner_function()
#
#
# outer_function()
#
# #=========
# def outer():
#     x = 1 #создаём локальную переменную
#     #объявляем внутреннюю функцию
#     def inner():
#         print('x in outer function: ', x)
#     #внешняя функция возвращает внутреннюю
#     return inner
#
# out = outer()
# print(out)
# out()
# outer()()
# #==========
# def saver():
#     kopilka=0
#     def adder(x):
#         nonlocal kopilka
#         kopilka+=x
#         return kopilka
#     return adder
# pig = saver()
# print(pig(25))
# print(pig(100))
# print(pig(19))
#
# #======
# def multiply_lst(lst):
#     if len(lst)==0:return 0
#     return lst[0]*multiply_lst(lst[1:])
#
# my_lst = [10, 21, 24, 12]
# print(multiply_lst(my_lst))
#
# #=======
# # Импортируем модуль для работы с системными переменными
# import sys
# # Увеличим глубину рекурсии
# sys.setrecursionlimit(1000000000)
#
# def factorial(n):
#     # Задаём условия выхода из рекурсии:
#     if n==0 or n==1: return 1
#     # Во всех других случаях возвращаем
#     # произведение текущего числа n и функции от n-1
#     return factorial(n-1)*n
#
# print(factorial(0))
# print(factorial(3))
# print(factorial(5))
#
# #=========
# #Продемонстрируем это с помощью функции time из модуля time. Она позволяет засечь время выполнения фрагмента кода (в нашем случае — вызова функции factorial).
# from time import time
# import sys
#
# sys.setrecursionlimit(1000000000)
#
# def factorial(n):
#     if n == 0: return 1
#     if n == 1: return 1
#     return factorial(n - 1) * n
#
# a = time()
# for i in range(100):
#     factorial(10000)
# b = time()
# print(b - a)
# # Будет напечатано:
# # 4.058465242385864
#
# #=========
# def fib(n):
#     if n == 0: return 0
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(8))
#
# #=======
# def power(i,n):
#     if n==0: return 1
#     if n==1: return i
#     return i*power(i,n-1)
#
# print("i=",power(3,4))
#
#
# #=======
# def get_total(units, price):
#     if units == 0: return 0
#     return price + get_total(units-1,price)
# print(get_total(15, 50))
#
# #=======
# def is_leap(year):
#     if (year%400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return True
#     else: return False
#
# print(is_leap(2000))
# print(is_leap(1900))
# print(is_leap(2020))
#
# print('=========')
# def check_date(day, month, year):
#     def is_leap(year):
#         if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#             return True
#         else:
#             return False
#     if type(year) is int and type(month) is int and type(day) is int:
#         if year >=1900 and year <=2022:
#             if (month >=1 and month <=12):
#                 if month in (4,9,11):
#                     if day >= 1 and day <= 30:
#                         return True
#                 if is_leap(year) and month == 2 and day <= 29 and day >= 1:
#                     return True
#                 if is_leap(year) is False and month == 2:
#                     if day <= 28 and day >= 1:
#                         return True
#                     else: return False
#                 if day >= 1 and day <= 31:
#                     return True
#     return False
# print(check_date(18,9,1999))
# print(check_date(29,2,2000))
# print(check_date(29,2,2021))
# print(check_date(13,13,2021))
# print(check_date(13.5,12,2021))
#
#
# print('====Задание 4.8=====')
#
# def check_date(day, month, year):
#     def is_leap(year):
#         if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#             return True
#         else:
#             return False
#     if type(year) is int and type(month) is int and type(day) is int:
#         if year >=1900 and year <=2022:
#             if (month >=1 and month <=12):
#                 if month in (4,9,11):
#                     if day >= 1 and day <= 30:
#                         return True
#                 if is_leap(year) and month == 2 and day <= 29 and day >= 1:
#                     return True
#                 if is_leap(year) is False and month == 2:
#                     if day <= 28 and day >= 1:
#                         return True
#                     else: return False
#                 if day >= 1 and day <= 31:
#                     return True
#     return False
# def register(surname, name, date, middle_name=None,registry=None):
#     if check_date(date[0],date[1],date[2]) is False:
#         raise ValueError('Invalid Date!')
#     if registry is None:
#         registry=list()
#     if len(registry)>0:
#         registry.append((surname, name, middle_name,date[0],date[1],date[2]))
#         return registry
#     registry.append((surname, name, middle_name,date[0],date[1],date[2]))
#     return registry
#
# reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
# print(reg)
# reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
# print(reg)
# reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
# print(reg)
#
#

print('===========')

def deposit(money, interest):
    # Процент по вкладу преобразуем во множитель:
    # делим процент на 100 и прибавляем 1
    interest = interest/100 + 1
    # Создаем бесконечный цикл
    while True:
        # Сумма вклада через год — это
        # текущая сумма, умноженная на коэффициент и
        # округлённая до двух знаков после запятой
        money = round(interest * money, 2)
        # Выдаём полученную сумму вклада
        yield money
bank = deposit(1000, 5)
print(next(bank)) # Запускаем генератор bank в первый раз
print(next(bank)) # Запускаем генератор bank во второй раз
print(next(bank)) # Запускаем генератор bank в третий раз


def deposit_years(money, interest, years):
    interest = interest/100 + 1
    # Вместо while используем цикл for с range
    for year in range(years):
        money = round(interest * money, 2)
        # Выдаём полученную сумму вклада
        yield money

bank2 = deposit_years(1500, 3, 2)
print(next(bank2))
print(next(bank2))




print('=====Задание 5.7======')
l = [101, 102, 103]
def inf_iter(l_in):
    while True:
        for i in l_in:
            yield i

gen = inf_iter(l)
for _ in range(10):
    print(next(gen))

print('=====Задание 5.8======')
def group_gen(n):
    while True:
        for i in range(1,n+1):
            yield i

gen = group_gen(4)
for _ in range(10):
    print(next(gen))
    
    
print('==========')
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 500) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

print('==========')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)