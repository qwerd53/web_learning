from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
from myapp.models import Users
def index(request):
    #print(reverse("myadd"))
    #print(reverse("thedate",args=(2003,1)))
    #执行Model操作

    #增
    # ob=Users()
    # ob.name="张三"
    # ob.age=18
    # ob.phone='1235533311'
    # ob.save()

    #u=Users(name='key',age=21,phone='123531451')
    #u.save()

    #删
    # mod=Users.objects#获取user的model对象
    # user=mod.get(id=6)
    # print(user.name)
    # user.delete()

    #改
    # ob=Users.objects.get(id=4)#获取user的model对象
    # ob.name='ravindi'
    # ob.age=22
    # ob.save()
    

    #查
    #ob=Users.objects
    #ulist=ob.all()
    #ulist=ob.filter(name='ravindi')
    # ulist=ob.filter(age__gt=20) #age大于20的
    # ulist=ob.filter(age__gte=20) #age大于等于20的
    # ulist=ob.filter(age__lte=20) #age小于等于20的
    #ulist=ob.order_by("age") #升序
    #ulist=ob.order_by("age")[0:3]

    #原生sql语句
    #ob=Users.objects.raw("select id=3") #不推荐写，不便于移植

    #for u in ulist:
        #print(u.id,u.name,u.age,u.phone,u.addtime)


    
    return HttpResponse('''
    <center> <h2>首页</h2> 
    <a href='/myapp/users'>用户信息管理</a>
    </center>
    ''')
    # return HttpResponse("hello world!")
def myadd(request):
     #重定向
    return(redirect(reverse("thedate",args=(2003,1))))
def find(request,year=0,month=0):

    return HttpResponse("hello the date is"+str(year)+str(month))


#浏览用户信息
def indexUsers(request):
    try:
        ulist=Users.objects.all()
        context={"userslist":ulist}
        return render(request,"myapp/users/index.html",context)#render用于加载模板
    except:
        return HttpResponse("没找到用户信息！")
#加载添加用户信息表单
def addUsers(request):
    return render(request,"myapp/users/add.html")
#执行用户信息添加
def insertUsers(request):
    try:
        ob=Users()
        ob.name=request.POST['name']
        ob.age=request.POST['age']
        ob.phone=request.POST['phone']
        ob.save()
        context={"info":"添加成功!"}
    except: 
        context={"info":"添加失败!"}
        
    return render(request,"myapp/users/info.html",context)

#执行用户信息删除
def delUsers(request,uid=0):
    try:
        ob=Users.objects.get(id=uid)
        ob.delete()#执行删除
        context={"info":"删除成功!"}
    except: 
        context={"info":"删除失败!"}
        
    return render(request,"myapp/users/info.html",context)

#加载用户信息修改表单
def editUsers(request,uid=0):
    try:
        ob=Users.objects.get(id=uid) #获取要修改的数据
        context={"user":ob}
        return render(request,"myapp/users/edit.html",context)
    except: 
        context={"info":"没有找到要修改的数据！"}
        return render(request,"myapp/users/info.html",context)

#执行用户信息修改
def updateUsers(request):
    try:
        uid= request.POST['id']#获取修改数据的 id号
        ob=Users.objects.get(id=uid)# 找到要修改的数据
        ob.name=request.POST['name']
        ob.age=request.POST['age']
        ob.phone=request.POST['phone']
        ob.save()
        context={"info":"修改成功!"}
    except:
        context={"info":"修改失败!"}
    return render(request,"myapp/users/info.html",context)
