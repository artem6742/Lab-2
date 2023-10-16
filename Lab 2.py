#задача 1
#ref_list = [[Иван,Игорь],[Cмирнов,Иванов]]
#print(ref_list[])


#задача 2

def del_rep(list):
    a = list(set(list))
    b = 0
    c = 0
    d = 0
    while True:
        if a[b] > a[b + 1]:
            c = a[b]
            a[b] = a[b + 1]
            a[b + 1] = c
        if a[b] < a[b + 1]:
            d += 1
        else:
            b = 0
        if b == len(a):
            break
        return a
    print(del_rep([1,2,1,3,1,4]))






#задача 4

# temp = int(input('уличная температура>>>')) #вводные данные
# условие
# if temp < -20:
#     print('холодно, менее -20')
# elif temp >= -20 and temp < 0:
#     print('прохладно')
# elif temp >= 0 and temp < 15:
#     print('зябко')
# elif temp >= 15 and temp <= 25:
#     print('тепло')
# elif temp > 25:
#     print('жарко')

#задача 5
#phones = ['+7 123 456 7890','8 904 678 8567','9827650928','0974365928']
#def check_phn:
#    print(len(phones))