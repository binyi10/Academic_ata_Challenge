__author__ = 'PC-2'
# -*- coding: utf-8 -*-
import csv
import numpy as np
#from sklearn.ensemble import RandomForestClassifier
############################################
#
#
#    统计每篇论文2011-2013，3年中的引用量
#
#
#############################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
file_year = open('D:/experiment/scholars_recongition/data/output/year.txt')
file_cite = open('D:/experiment/scholars_recongition/data/output/cite_2011_2013.txt','a',encoding="utf-8")
file_cite_name = open('D:/experiment/scholars_recongition/data/output/cite_2011_2013_name.txt','a',encoding="utf-8")
line = file_object.readline()
year = file_year.readline()
citation = {}
i = 0
while line:
    year = int(year)
    if year <= 2013 and year >= 2011 :
        l = line.split("#%")
        if len(l) > 1 :
            del l[0]
            for ll in l:
                ll = int(ll.split(",")[0])
                if ll not in citation:
                    citation[ll] = 0
                citation[ll] += 1
    line = file_object.readline()
    year = file_year.readline()
##########################################存档

# for cite in citation:
#     file_cite_name.write(str(cite))
#     file_cite_name.write('\n')
#     file_cite.write(str(citation[cite]))
#     file_cite.write('\n')

###########################################
file_object.close()
file_year.close()
file_cite.close()
file_cite_name.close()
##########################################################################
#
#
#  统计2013年前总的引用量，并用之前统计的2011-2013的估计2013-2017年的引用量
#
#
###########################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
file_year = open('D:/experiment/scholars_recongition/data/output/year.txt')
#file_cite1 = open('D:/experiment/scholars_recongition/data/output/cite_all.txt','a',encoding="utf-8")
#file_cite_name1 = open('D:/experiment/scholars_recongition/data/output/cite_all_name.txt','a',encoding="utf-8")
line = file_object.readline()
year = file_year.readline()
citation_all = {}
while line:
    year = int(year)
    if year <= 2013:
        l = line.split("#%")
        if len(l) > 1 :
            del l[0]
            for ll in l:
                ll = int(ll.split(",")[0])
                if ll not in citation_all:
                    citation_all[ll] = 0
                citation_all[ll] += 1
    line = file_object.readline()
    year = file_year.readline()
for cite in citation_all:
    if cite in citation:
        citation_all[cite] += int((citation[cite]*4/3))
# for cite in citation_all:
#      file_cite_name1.write(str(cite))
#      file_cite_name1.write('\n')
#      file_cite1.write(str(citation_all[cite]))
#      file_cite1.write('\n')
file_object.close()
file_year.close()

##########################################################################
#
#
#  统计每个人的总引用量（根据文章）
#
#
###########################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
file_year = open('D:/experiment/scholars_recongition/data/output/year.txt')
#file_cite2 = open('D:/experiment/scholars_recongition/data/output/people_name.txt','a',encoding="utf-8")
#file_cite_name2 = open('D:/experiment/scholars_recongition/data/output/people_cite.txt','a',encoding="utf-8")
line = file_object.readline()
year = file_year.readline()
i = 0
people_citation = {}
while line:
     l = line.split("#@")
     if len(l) > 1:
         l = l[1]
         l = l.split(",#*")[0]
         l = l.split(",")
         for ll in l:
             if ll not in people_citation:
                 people_citation[ll] = 0
             if i in citation_all:
                 people_citation[ll] += citation_all[i]
     i += 1
     line = file_object.readline()
# for cite in people_citation:
#     file_cite_name2.write(str(cite))
#     file_cite_name2.write('\n')
#     file_cite2.write(str(people_citation[cite]))
#     file_cite2.write('\n')
file_object.close()
file_year.close()

print("ready to caculate the number of citation of each people")
with open('D:/experiment/scholars_recongition/data/task3/train.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
predict_num = []
del rows[0]
for row in rows:
    name = row[0]
    predict_num.append(people_citation[name])
print(predict_num[0:100])
#file_pre = open('D:/experiment/scholars_recongition/data/output/pre.txt','a',encoding="utf-8")
# for i in predict_num:
#     file_pre.write(str(i))
#     file_pre.write('\n')
with open('D:/experiment/scholars_recongition/data/task3/validation.csv','r',encoding="utf-8") as fi:
    reader = csv.reader(fi)
    rows = [row for row in reader]
va_num = []
del rows[0]
for row in rows:
    name = row[0]
    n = people_citation[name]
    va_num.append(n)
print(va_num[0:100])
print(va_num.count(0))

# file_pre = open('D:/experiment/scholars_recongition/data/output/va_num.txt','a',encoding="utf-8")
# for i in va_num:
#     file_pre.write(str(i))
#     file_pre.write('\n')
# with open('D:/experiment/scholars_recongition/data/output/re.txt','a',encoding="utf-8") as fil:
#     i = 0
#     for row in rows:
#         fil.write(row[0]+'\t'+str(va_num[i])+'\n')
#         i += 1
##########################################################################
#
#
#  统计每个人被引用的最多的文章的引用数目
#
#
###########################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
line = file_object.readline()
i = 0
people_citation_max = {}
while line:
     l = line.split("#@")
     if len(l) > 1:
         l = l[1]
         l = l.split(",#*")[0]
         l = l.split(",")
         for ll in l:
             if ll not in people_citation_max:
                 people_citation_max[ll] = 0
             if i in citation_all:
                 people_citation_max[ll] = max(people_citation_max[ll],citation_all[i])
     i += 1
     line = file_object.readline()
file_object.close()
with open('D:/experiment/scholars_recongition/data/task3/train.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
max_cite = []
del rows[0]
for row in rows:
    name = row[0]
    if name in people_citation_max:
        max_cite.append(people_citation_max[name])
    else:
        max_cite.append(0)
file_pre = open('D:/experiment/scholars_recongition/data/output/max_cite.txt','a',encoding="utf-8")
for i in max_cite:
    file_pre.write(str(i))
    file_pre.write('\n')

with open('D:/experiment/scholars_recongition/data/task3/validation.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows_vali = [row for row in reader]
va_max_cite = []
del rows_vali[0]
for row in rows_vali:
    name = row[0]
    if name in people_citation_max:
        va_max_cite.append(people_citation_max[name])
    else:
        va_max_cite.append(0)
file_pre = open('D:/experiment/scholars_recongition/data/output/va_max_cite.txt','a',encoding="utf-8")
for i in va_max_cite:
    file_pre.write(str(i))
    file_pre.write('\n')



##########################################################################
#
#
#  统计每个人被引用的最少的文章的引用数目
#
#
###########################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
line = file_object.readline()
i = 0
people_citation_min = {}
while line:
     l = line.split("#@")
     if len(l) > 1:
         l = l[1]
         l = l.split(",#*")[0]
         l = l.split(",")
         for ll in l:
             if ll not in people_citation_min:
                 people_citation_min[ll] = 0xffffff
             if i in citation_all:
                 people_citation_min[ll] = min(people_citation_max[ll],citation_all[i])
             else:
                 people_citation_min[ll] = 0
     i += 1
     line = file_object.readline()
file_object.close()
with open('D:/experiment/scholars_recongition/data/task3/train.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
min_cite = []
del rows[0]
for row in rows:
    name = row[0]
    if name in people_citation_min:
        if people_citation_min[name] != 0xffffff:
            min_cite.append(people_citation_min[name])
        else:
            min_cite.append(0)
    else:
        min_cite.append(0)
file_pre = open('D:/experiment/scholars_recongition/data/output/min_cite.txt','a',encoding="utf-8")
for i in min_cite:
    file_pre.write(str(i))
    file_pre.write('\n')

with open('D:/experiment/scholars_recongition/data/task3/validation.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows_vali = [row for row in reader]
va_min_cite = []
del rows_vali[0]
for row in rows_vali:
    name = row[0]
    if name in people_citation_min:
        if people_citation_min[name] != 0xffffff:
            va_min_cite.append(people_citation_min[name])
        else:
            va_min_cite.append(0)
    else:
        va_min_cite.append(0)
file_pre = open('D:/experiment/scholars_recongition/data/output/va_min_cite.txt','a',encoding="utf-8")
for i in va_min_cite:
    file_pre.write(str(i))
    file_pre.write('\n')
##########################################################################
#
#
#  统计每个人被引用的文章的中位数引用数目
#
#
###########################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
line = file_object.readline()
i = 0
people_citation_median_l = {}
while line:
     l = line.split("#@")
     if len(l) > 1:
         l = l[1]
         l = l.split(",#*")[0]
         l = l.split(",")
         for ll in l:
             if ll not in people_citation_median_l:
                 people_citation_median_l[ll] = []
             if i in citation_all:
                 people_citation_median_l[ll].append(citation_all[i])
             else:
                 people_citation_median_l[ll].append(0)
     i += 1
     line = file_object.readline()
file_object.close()
people_citation_median = {}
for p in people_citation_median_l:
    if len(people_citation_median_l[p]) > 0:
        people_citation_median[p] = np.median(people_citation_median_l[p])
    else :
        people_citation_median[p] = 0
with open('D:/experiment/scholars_recongition/data/task3/train.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
median_cite = []
del rows[0]
for row in rows:
    name = row[0]
    if name in people_citation_median:
        median_cite.append(people_citation_median[name])
    else:
        median_cite.append(0)
file_pre = open('D:/experiment/scholars_recongition/data/output/median_cite.txt','a',encoding="utf-8")
for i in median_cite:
    file_pre.write(str(i))
    file_pre.write('\n')

with open('D:/experiment/scholars_recongition/data/task3/validation.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows_vali = [row for row in reader]
va_median_cite = []
del rows_vali[0]
for row in rows_vali:
    name = row[0]
    if name in people_citation_median:
        va_median_cite.append(people_citation_median[name])
    else:
        va_median_cite.append(0)
file_pre = open('D:/experiment/scholars_recongition/data/output/va_median_cite.txt','a',encoding="utf-8")
for i in va_median_cite:
    file_pre.write(str(i))
    file_pre.write('\n')

#######################################
#
#
#   统计每个人2013年之前发文章的总数目
#
#
#######################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
file_year = open('D:/experiment/scholars_recongition/data/output/year.txt')
line = file_object.readline()
year = file_year.readline()
people_work = {}
while line:
    year = int(year)
    if year <= 2013:
        l = line.split("#@")
        if len(l) > 1:
            l = l[1]
            l = l.split(",#*")[0]
            l = l.split(",")
            for ll in l:
                if ll not in people_work:
                    people_work[ll] = 0
                people_work[ll] += 1
    line = file_object.readline()
    year = file_year.readline()
file_object.close()
file_year.close()
####################################################################
#
#
#   统计每个人2011-2013年之前发文章的总数目,作为2014-2017文章总数的参考
#
#
####################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
file_year = open('D:/experiment/scholars_recongition/data/output/year.txt')
line = file_object.readline()
year = file_year.readline()
people_work_2011 = {}
while line:
    year = int(year)
    if year <= 2013 and year >= 2011:
        l = line.split("#@")
        if len(l) > 1:
            l = l[1]
            l = l.split(",#*")[0]
            l = l.split(",")
            for ll in l:
                if ll not in people_work_2011:
                    people_work_2011[ll] = 0
                people_work_2011[ll] += 1
    line = file_object.readline()
    year = file_year.readline()
file_object.close()
file_year.close()
####################################################################
#
#
#   预测每个人2014-2017发文章的总数，并且加上13年以前的
#
#
####################################################################
people_pre = {}
for p in people_work:
    if p in people_work_2011:
        people_pre[p] = people_work[p] + int(people_work_2011[p]*4/3)
    else:
        people_pre[p] = people_work[p]
with open('D:/experiment/scholars_recongition/data/task3/train.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
total_work = []
del rows[0]
for row in rows:
    name = row[0]
    if name in people_pre:
        total_work.append(people_pre[name])
    else:
        total_work.append(0)
print(total_work[0:100])
# file_pre = open('D:/experiment/scholars_recongition/data/output/total_work.txt','a',encoding="utf-8")
# for i in total_work:
#     file_pre.write(str(i))
#     file_pre.write('\n')
####################################################################
#
#
#   记录作者最早的发文时间
#
#
####################################################################
file_object = open('D:/experiment/scholars_recongition/data/task3/papers2.txt',encoding="utf-8")
file_year = open('D:/experiment/scholars_recongition/data/output/year.txt')
line = file_object.readline()
year = file_year.readline()
people_year = {}
while line:
    year = int(year)
    l = line.split("#@")
    if len(l) > 1:
        l = l[1]
        l = l.split(",#*")[0]
        l = l.split(",")
        for ll in l:
            if ll not in people_year:
                people_year[ll] = year
            else:
                people_year[ll] = min(people_year[ll],year)
    line = file_object.readline()
    year = file_year.readline()
file_object.close()
file_year.close()
with open('D:/experiment/scholars_recongition/data/task3/train.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
pp_year = []
del rows[0]
for row in rows:
    name = row[0]
    if name in people_year:
        pp_year.append(people_year[name])
    else:
        pp_year.append(2013)
print(pp_year[0:100])


# file_pre = open('D:/experiment/scholars_recongition/data/output/people_year.txt','a',encoding="utf-8")
# for i in pp_year:
#     file_pre.write(str(i))
#     file_pre.write('\n')

####################################################################
#
#
#   处理测试集数据,写测试集数据日期
#
#
####################################################################
with open('D:/experiment/scholars_recongition/data/task3/validation.csv','r',encoding="utf-8") as fi:
    reader = csv.reader(fi)
    rows_vali = [row for row in reader]
del rows_vali[0]



va_pp_year = []
for row in rows_vali:
    name = row[0]
    if name in people_year:

        va_pp_year.append(people_year[name])
    else:
        va_pp_year.append(2013)
print(va_pp_year[0:100])
# file_pre = open('D:/experiment/scholars_recongition/data/output/va_people_year.txt','a',encoding="utf-8")
# for i in va_pp_year:
#     file_pre.write(str(i))
#     file_pre.write('\n')
####################################################################
#
#
#   处理测试集数据,写估计发布的论文数目
#
#
####################################################################
va_total_work = []
for row in rows_vali:
    name = row[0]
    if name in people_pre:
        va_total_work.append(people_pre[name])
    else:
        va_total_work.append(0)
print(va_total_work[0:100])
# file_pre = open('D:/experiment/scholars_recongition/data/output/va_total_work.txt','a',encoding="utf-8")
# for i in va_total_work:
#     file_pre.write(str(i))
#     file_pre.write('\n')