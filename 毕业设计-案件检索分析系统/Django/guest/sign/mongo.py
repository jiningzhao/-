from pymongo import MongoClient
from sign import constant
import re

conn=MongoClient(host='127.0.0.1',port=27017)
db=conn.mydb
test1=db.test1
master=db.master
cover_master=db.cover_master
min_DB=db.min_DB
XS_DB=db.XS_DB
XZ_DB=db.XZ_DB
Special_DB=db.Special_DB
area_DB=db.area_DB


def INSERT_DB(data):
    for i in master.find({'no':data['no']}):
        constant.id=i["no"]
    if constant.id == "0":
        master.insert(data)
        return constant.jump0
    else:
        constant.id = "0"
        return constant.jump1



def INSERT_DB_MAX(data):
    master.insert(data)
    return constant.jump0

def REMOVE_DB():#删除数据库
    master.remove()

def COVER_MASTER():#备份数据库
    cover_master.remove()
    for i in master.find():
        cover_master.insert(i)
def Pie_DB():     #数据可视化所用数据统计
    number_min=0
    number_XS=0
    number_XZ=0
    number_Special=0
    for i1 in master.find({"type_key":"民事案件"}):
        number_min+=1
    for i2 in master.find({"type_key":"刑事案件"}):
        number_XS+=1
    for i3 in master.find({"type_key":"行政案件"}):
        number_XZ+=1
    for i4 in master.find({"type_key":"特殊案件"}):
        number_Special+=1
    return number_min,number_XS,number_XZ,number_Special
def Histogram_DB():  # 数据可视化所用数据统计
    k1=[0,0,0]
    k2=[0,0,0]
    k3=[0,0,0]
    k4=[0,0,0]
    for i1 in master.find({"season":"春季"}):
        k1[0]+=1
    for i2 in master.find({"$and":[{"season":"春季"},{"make":"已侦破"}]}):
        k1[1]+=1
    for i3 in master.find({"$and":[{"season":"春季"},{"make":"未侦破"}]}):
        k1[2]+=1

    for j1 in master.find({"season":"夏季"}):
        k2[0]+=1
    for j2 in master.find({"$and":[{"season":"夏季"},{"make":"已侦破"}]}):
        k2[1]+=1
    for j3 in master.find({"$and":[{"season":"夏季"},{"make":"未侦破"}]}):
        k2[2]+=1

    for m1 in master.find({"season":"秋季"}):
        k3[0]+=1
    for m2 in master.find({"$and":[{"season":"秋季"},{"make":"已侦破"}]}):
        k3[1]+=1
    for m3 in master.find({"$and":[{"season":"秋季"},{"make":"未侦破"}]}):
        k3[2]+=1

    for p1 in master.find({"season":"冬季"}):
        k4[0]+=1
    for p2 in master.find({"$and":[{"season":"冬季"},{"make":"已侦破"}]}):
        k4[1]+=1
    for p3 in master.find({"$and":[{"season":"冬季"},{"make":"未侦破"}]}):
        k4[2]+=1
    return k1,k2,k3,k4
def Line_DB():  # 数据可视化所用数据统计
    k1=[0,0,0,0,0,0,0,0,0,0,0,0]
    k2=[0,0,0,0,0,0,0,0,0,0,0,0]
    k3=[0,0,0,0,0,0,0,0,0,0,0,0]
    k4=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in master.find():
        for j in range(1,13):
            m=int(i["date"][5:7])
            if m == j :
                if i["type_key"] == "民事案件":
                    k1[j-1] += 1
                if i["type_key"] == "刑事案件":
                    k2[j-1] += 1
                if i["type_key"] == "行政案件":
                    k3[j-1] += 1
                if i["type_key"] == "特殊案件":
                    k4[j-1] += 1
    return k1,k2,k3,k4
def China_DB():  # 数据可视化所用数据统计
    table=constant.table
    table_dict1=constant.table_dict1
    table_dict2=constant.table_dict2
    table_dict3=constant.table_dict3
    table_dict4=constant.table_dict4
    for i in master.find():
        for j in table:
            if i["area_key"][0:-1] == j and i["type_key"] == "民事案件":
                table_dict1[j]=0
            if i["area_key"][0:-1] == j and i["type_key"] == "刑事案件":
                table_dict2[j]=0
            if i["area_key"][0:-1] == j and i["type_key"] == "行政案件":
                table_dict3[j]=0
            if i["area_key"][0:-1] == j and i["type_key"] == "特殊案件":
                table_dict4[j]=0
    for i in master.find():
        for j in table:
            if i["area_key"][0:-1] == j and i["type_key"] == "民事案件":
                table_dict1[j]+=1
            if i["area_key"][0:-1] == j and i["type_key"] == "刑事案件":
                table_dict2[j]+=1
            if i["area_key"][0:-1] == j and i["type_key"] == "行政案件":
                table_dict3[j]+=1
            if i["area_key"][0:-1] == j and i["type_key"] == "特殊案件":
                table_dict4[j]+=1
    return table_dict1,table_dict2,table_dict3,table_dict4
def Select_delate_fix(sel):
    form=[]
    if sel == '':
        for i in master.find():
            form.append(dict(i))
        return form
    else:
        for i in master.find({'$or':[{"name":sel},{"area_key":sel},
                                     {"area_value":sel},{"type_key":sel},
                                     {"type_value":sel},{"no":sel},{"date":sel},
                                     {"season":sel}]}):
            form.append(dict(i))
        return form
def Delate(data):
    master.remove({"no":data})
    return 0
def Fix(data):
    print(data)
    master.update({"no":data["no"]},{"$set":data["value"]})
    return 0