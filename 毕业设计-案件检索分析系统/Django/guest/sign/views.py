from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign import mongo
from sign import constant,DBDBDBDBDBDBDBDB

# Create your views here.
def index(request):
    request.session.clear()
    return render(request,'index.html')

def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username',str) #通过post接受前端传入的信息
        password=request.POST.get('password',str)
        user=auth.authenticate(username=username,password=password) #判断是否存在该账号，及该账号的密码是否正确
        if user is not None:
            auth.login(request,user) #登陆
            response=HttpResponseRedirect('/menu/') #跳转到/menu/链接
            request.session['user']=username    #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})#错误状态下跳转回当前页面，并给出错误提示
@login_required       # 未登录的状态无法访问该页面
def menu(request):
    username=request.session.get('user',str)
    return render(request, 'menu.html',{'user':username})

@login_required       # 未登录的状态无法访问该页面
def Insert(request):
    if request.method == 'POST':   # 判断前端表单是否进行post提交
        no=request.POST.get('no',str)
        name=request.POST.get('name',str)
        type_key=request.POST.get('type_key',str)
        type_value=request.POST.get('type_value',str)
        area_key=request.POST.get('area_key',str)
        area_value=request.POST.get('area_value',str)
        season=request.POST.get('season',str)
        date=request.POST.get('date',str)
        make=request.POST.get('make',str)
        # 数据处理
        data={"no":no,"name":name,"type_key":type_key,"type_value":type_value,
              "area_key":area_key,"area_value":area_value,"season":season,"date":date,"make":make}
        jump=mongo.INSERT_DB(data) # 调用mongo模块的INSERT_DB方法进行数据插入
        return render(request,'Insert.html',{'jump':jump})
    else:                         # 未进行表单提交，单纯显示前端页面
        return render(request, 'Insert.html')


@login_required
def Cover(request):#一键备份数据
    mongo.COVER_MASTER()
    return render(request, 'Insert.html')


@login_required
def Insert_max_data(request):#一键造数据
    DBDBDBDBDBDBDBDB.Insert_max_data()
    return render(request, 'Insert.html')



@login_required       # 未登录的状态无法访问该页面
def Select_delate_fix(request):#查询修改删除数据
    username = request.session.get('user', str)
    if request.method == "POST":
        constant.sel = request.POST.get('select',str)
        data1 = mongo.Select_delate_fix(constant.sel)
        return render(request, 'select_delate_fix.html', {'user': username, 'data': data1})
    else:
        constant.sel = ""
        data1=mongo.Select_delate_fix(constant.sel)[0:18]
        print(data1)
        return render(request, 'select_delate_fix.html',{'user':username,'data':data1})



@login_required       # 未登录的状态无法访问该页面
def Pie(request):
    username=request.session.get('user',str)
    a,b,c,d=mongo.Pie_DB()
    data=[a,b,c,d]
    return render(request, 'pie.html',{'user':username,"data":data})
@login_required       # 未登录的状态无法访问该页面
def Line(request):
    username=request.session.get('user',str)
    k1,k2,k3,k4=mongo.Line_DB()
    data=[k1,k2,k3,k4]
    return render(request, 'line.html',{'user':username,"data":data})


@login_required       # 未登录的状态无法访问该页面
def Histogram(request):
    username=request.session.get('user',str)
    k1,k2,k3,k4=mongo.Histogram_DB()
    k0=['product', '总量', '已侦破', '未侦破']
    k1=['春季', k1[0], k1[1], k1[2]]
    k2=['夏季', k2[0], k2[1], k2[2]]
    k3=['秋季', k3[0], k3[1], k3[2]]
    k4=['冬季', k4[0], k4[1], k4[2]]
    data=[k0,k1,k2,k3,k4]
    return render(request, 'histogram.html',{'user':username,"data":data})

@login_required       # 未登录的状态无法访问该页面
def China(request):
    username=request.session.get('user',str)
    value=value1=value2=value3=value4=[]
    k1,k2,k3,k4=mongo.China_DB()
    value1=list(k1.values())
    value2=list(k2.values())
    value3=list(k3.values())
    value4=list(k4.values())
    value=[value1,value2,value3,value4]
    return render(request, 'china.html',{'user':username,"value":value})
@login_required       # 未登录的状态无法访问该页面
def Details(request):
    username=request.session.get('user',str)
    name=request.GET.get("name",str)
    k=mongo.Select_delate_fix(name)
    data={"name":name,"number":len(k),"list":k}
    return render(request, 'Details.html',{'user':username,"data":data})
@login_required       # 未登录的状态无法访问该页面
def Fix(request):
    if request.method == "POST":
        no = request.POST.get('no', str)
        name = request.POST.get('name', str)
        type_key = request.POST.get('type_key', str)
        type_value = request.POST.get('type_value', str)
        area_key = request.POST.get('area_key', str)
        area_value = request.POST.get('area_value', str)
        season = request.POST.get('season', str)
        date = request.POST.get('date', str)
        make = request.POST.get('make', str)
        value = {"no": no, "name": name, "type_key": type_key, "type_value": type_value, "area_key": area_key,
                "area_value": area_value, "season": season, "date": date, "make": make}
        data={"no":no,"value":value}
        mongo.Fix(data)
        return HttpResponseRedirect('/select_delate_fix/')
    else:
        no = request.GET.get('no', str)
        k=mongo.Select_delate_fix(no)[0]
        return render(request, 'Fix.html', {'data': k})
@login_required       # 未登录的状态无法访问该页面
def Delate(request):
    no=request.GET.get('no',str)
    mongo.Delate(no)
    constant.sel = ""
    data1 = mongo.Select_delate_fix(constant.sel)[0:18]
    # return render(request, 'select_delate_fix.html',{"data":data1})
    return HttpResponseRedirect('/select_delate_fix/')