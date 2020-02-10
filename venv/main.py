#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on 29.11.19

:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""


import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import time
import datetime
from datetime import date
#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox)
#import PyQt5
import math
import unicodedata

end_list = [[]]


class global_params():
    url_file = os.getcwd() + "/AccessLog 29 01 2020.txt"
    all_list = []
    calc_list_ = []
    cardlist = [['220-26857', ' Vadchenko Anna'], ['115-54089', 'Bazirca Artiom'], ['207-41001', 'Belii Mihail'],
                ['180-14233', 'Bercaru Ion'], ['219-53897', 'Beznitchi Oleg'], ['193-33961', 'Bologov Vasilii'],
                ['185-04537', 'Boncev Gleb'], ['140-15401', 'Braniste Daniela'], ['032-34793', 'Brasoveanu Andrei'],
                ['195-56777', 'Bulgaru Veaceslav'], ['093-21465', 'Caraiman Elena'], ['011-18217', 'Caun Dmitrii'],
                ['226-02985', 'Cebanu Anton'], ['199-43910', 'Ciobanu Mihai'], ['243-64569', 'Cojuhari Daniel'],
                ['225-55945', 'Corneeva Ecaterina'], ['131-35593', 'Damaschin  Lucia'], ['217-16665', 'Efros  Daria'],
                ['059-53256', 'Ernest'], ['088-12137', 'Esanu Nick'], ['072-18697', 'Faraji Emili'],
                ['055-32930', 'Fazylova Aida'], ['085-22630', 'Fazylova Aida'], ['198-42137', 'Fortuna Vlad'],
                ['030-08361', 'Galaju Margareta'], ['179-22217', 'Ghetmanet Patrisia'], ['248-64089', 'Giter Vsevolod'],
                ['255-05017', 'Gorobivschii Dorin'], ['029-53129', 'Guritanu Andrei'], ['099-44808', 'Guritanu Andrei'],
                ['170-06617', 'Hacico  Nicolai'], ['174-53145', 'Husnulin Vladimir'], ['044-53138', 'Ialanji Alexandr'],
                ['070-40793', 'Ialovenco Irina'], ['018-06214', 'Jane'], ['136-53225', 'Manolov Nicolai'],
                ['057-12201', 'Marcov Sergei'], ['012-34345', 'Markov Serghei'], ['056-13074', 'Mihaela'],
                ['034-16345', 'Muntean Andrei'], ['029-56009', 'Naperkovski Dima'], ['224-34905', 'Ojo George'],
                ['026-57417', 'Ojo Michael'], ['032-34793', 'Oprea Daria'], ['055-00210', 'Orlova Jane'],
                ['000-42553', 'Papkova Nelli'], ['242-58153', 'Perkin Gena'], ['154-32489', 'Petrenco Ksenia'],
                ['120-31673', 'Popa Eugen'], ['056-33282', 'Pricolota Alexei'], ['205-01001', 'Pricolota Alexei'],
                ['009-36969', 'Racu Oleg'], ['214-18105', 'Rodion'], ['227-04985', 'Rosca Ecaterina'],
                ['049-33913', 'Savin Efim'], ['040-23602', 'Schiopu Simion'], ['237-26041', 'Sevastianova Victoria'],
                ['208-51065', 'Slav Antonina'], ['014-47065', 'Svet Ernest'], ['221-24649', 'Svet Ernest'],
                ['252-39657', 'Tatiana Genadievna'], ['253-62518', 'top noci Sasha'],
                ['013-53753', 'Tsyguleova Tatiana'], ['071-60537', 'Tulum Pavel'], ['180-52441', 'uesr 1'],
                ['113-46073', 'Ungureanu Aurel'], ['017-06713', 'user 2'], ['237-06553', 'user 3'],
                ['227-02137', 'user4'], ['157-21385', 'user5'], ['012-49913', 'Zagadailova Iulia'],
                ['150-41353', 'Zagorschi  Victor'], ['101-18297', 'Zalevschi Vladislav']]

class day_count():
    date_num = ''
    day_names = []
    day_cell = []



def calc_time_teacking_day(url):

    calc_list_ = []
    # перекодировать файл в utf-8

    # открыли файл, считали строки
    file = open(url, 'r')
    lines_file = file.readlines()
    file.close()
    lines_file = [line.rstrip() for line in lines_file]
    lines_file = [line.replace(', ', ',') for line in lines_file]
    lines_file = [line.replace('"', '') for line in lines_file]
    c = len(lines_file)
    while c > 0:
        str1_list1 = lines_file[c-1].split(',')
        str1 = []
        str1.append(str1_list1[5])
        str1.append(str1_list1[4])
        str1.append(str1_list1[3])
        str1.append(str1_list1[2])
        global_params.calc_list_.append(str1)
        #print(str_list)
        c-=1
    t = 0
    time_n = ""
    t_S = 12
    time_n = str(t_S)
    while t < len(global_params.calc_list_):
        s = global_params.calc_list_[t][2]
        #print(s)
        s_l = s.split(' ')
        if s_l[2] == 'AM':
            #print("morning")
            s_time = s_l[1].split(':')
            #print(s_time[0])
            d_time = s_l[0].split('/')
            if s_time[0] == '12':
                s_time[0] = '24'
                d = d_time[1]
                n_d = int(d)-1
                s_l[0] = d_time[0] +'/'+ str(n_d) +'/'+ d_time[2]
            if s_time[0] == '1':
                s_time[0] = '25'
                s_time[0] = '24'
                d = d_time[1]
                n_d = int(d) - 1
                s_l[0] = d_time[0] + '/' + str(n_d) + '/' + d_time[2]
            if s_time[0] == '2':
                s_time[0] = '26'
                s_time[0] = '24'
                d = d_time[1]
                n_d = int(d) - 1
                s_l[0] = d_time[0] + '/' + str(n_d) + '/' + d_time[2]
            if s_time[0] == '3':
                s_time[0] = '27'
                s_time[0] = '24'
                d = d_time[1]
                n_d = int(d) - 1
                s_l[0] = d_time[0] + '/' + str(n_d) + '/' + d_time[2]
            if s_time[0] == '4':
                s_time[0] = '28'
                s_time[0] = '24'
                d = d_time[1]
                n_d = int(d) - 1
                s_l[0] = d_time[0] + '/' + str(n_d) + '/' + d_time[2]
            new_time_ = s_time[0]+":"+s_time[1]+":"+s_time[2]
            #print(new_time_)
            s_l[1] = new_time_

        if s_l[2] == 'PM':
            #print('evening')
            s_time1 = s_l[1].split(':')
            #print(s_time1[0])

            if s_time1[0] != '12':
                t_S = int(s_time1[0]) + 12

                time_n = str(t_S)

            else:
                time_n = "12"
            s_time1[0] = time_n
            new_time_1 = s_time1[0]+":"+s_time1[1]+":"+s_time1[2]
            #print(new_time_1)
            s_l[1] = new_time_1
        new_s_l = s_l[0] + " " + s_l[1]
        #print(new_s_l)
        global_params.calc_list_[t][2] = new_s_l
        t+=1

    #print(global_params.calc_list_)
    date_ = global_params.calc_list_[0][2]
    date_1 = date_.split(' ')
    day_count.date_num = date_1[0]
    print(global_params.calc_list_[len(global_params.calc_list_)-1][2])

    ds = date_1[0].split('/')
    start_day = int(ds[1])


    date_ = global_params.calc_list_[len(global_params.calc_list_)-1][2]
    date_1 = date_.split(' ')
    ds = date_1[0].split('/')

    last_day = int(ds[1])


    print(start_day, last_day)

    d_coin = start_day

    while d_coin < last_day+1:
        day_count.date_num = str(d_coin)
        """st_start = 0
        st_end = 0
        p = 0
        while p < len(global_params.calc_list_):

            a1 = global_params.calc_list_[p][2]
            a1 = a1.split(' ')
            a1 = a1[0].split('/')
            a1 = a1[1]
            if a1 == d_coin:
                print(a1)


            p+=1"""
        end_list[0].append(str(d_coin))

        j = 0
        while j < len(global_params.cardlist):

            # print(global_params.cardlist[j][1])
            day_count.day_names.append(global_params.cardlist[j][1])
            k = 0
            r = 0
            ti = 0
            
            while k < len(global_params.calc_list_):

                a1 = global_params.calc_list_[k][2]
                a1 = a1.split(' ')
                a1 = a1[0].split('/')
                a1 = int(a1[1])
                #print(a1)
                if a1 == d_coin:
                    ti_r = 0
                    if (global_params.cardlist[j][0] == global_params.calc_list_[k][0]):
                        # print(global_params.calc_list_[k][3], global_params.calc_list_[k][2])
                        if global_params.calc_list_[k][3] == 'Внутрь':
                            try:
                                r = k
                                # print('        запомнил вход')
                            except:
                                print("error")
                        if global_params.calc_list_[k][3] == 'Наружу':
                            try:
                                # print("  Время входа")
                                # print(global_params.calc_list_[r][2])
                                # print("  Время выхода")
                                # print(global_params.calc_list_[k][2])

                                s_in = global_params.calc_list_[r][2].split(' ')
                                s_out = global_params.calc_list_[k][2].split(' ')

                                # print(s_out[1] + " - " + s_in[1])

                                t_in = s_in[1].split(':')
                                t_out = s_out[1].split(':')
                                if t_out[0] == "0":
                                    t_out[0] = "24"

                                # print(t_in, t_out)

                                ti_in = int(t_in[0]) * 60 * 60 + int(t_in[1]) * 60 + int(t_in[2])
                                ti_out = int(t_out[0]) * 60 * 60 + int(t_out[1]) * 60 + int(t_out[2])
                                # print(ti_out, ti_in)
                                ti_r = ti_out - ti_in
                                # print("время круга "+ str(ti_r))
                                # print("общее время " +str(ti))
                            except:
                                print("error")
                    ti = ti + ti_r
                

                k += 1
            # print("====== Был на месте " + str(ti) + "  секунд")

            ti = ti / 60
            ti = ti / 60
            # print("часов " + str(ti))
            ti = round(ti, 2)
            day_count.day_cell.append(ti)
            j += 1

        #print(day_count.date_num)
        w = 0
        while w < len(day_count.day_names):
            #print(day_count.day_names[w] + '  ' + day_count.date_num + '  был на месте  ' + str(day_count.day_cell[w]) + '  часов ')
            end_list[w+1].append(str(day_count.day_cell[w]))


            w += 1
        day_count.date_num = ''
        day_count.day_names = []
        day_count.day_cell = []

        d_coin += 1




    print("end")




t_ = str(datetime.datetime.today())
print(t_)

end_list[0].append('                             ')
j = 0
while j < len(global_params.cardlist):
    x = []
    x.append(global_params.cardlist[j][1])
    end_list.append(x)
    j+=1






calc_time_teacking_day(global_params.url_file)

p =  os.getcwd() + "/newX 29.01.20 new.csv"
f_new = open(p, 'w')

i = 0
while i < len(end_list):
    print(end_list[i])
    g = 0
    s = ''
    while g < len(end_list[i]):
        s += end_list[i][g] + ';'
        g+=1
    s += '\n'
    f_new.write(s)
    print(s)
    i+=1

f_new.close()
"""
w = 0
while w < len(day_count.day_names):
    print(day_count.day_names[w] +'  '+day_count.date_num+'  был на месте  '+ str(day_count.day_cell[w]) + '  часов ')
    w+=1"""







# составление списка карт
"""pfile = os.getcwd() + "/CardList .csv"
file = open(pfile, 'r')
f = file.readlines()
file.close()
f = [line.rstrip() for line in f]
i = 0
s = []
while i < len(f):
    s.append(f[i].split(','))
    i+=1
print(s)
"""

























