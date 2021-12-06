from django.shortcuts import render

def welcome(request):
    data="helloworld"
    return render(request,'welcome.html',{'data':data})

def multi(request):
    data="helloworld"
    data1=['pyspiders','python','django']
    data2=('Qspiders','testing','java')
    data3={'jspiders','java','spring'}
    data4={'a':'python','b':'django'}
    data5=10
    data6=(10+3j)
    return render(request,'multi.html',{'data':data,'data1':data1,
                                          'data2':data2,'data3':data3,
                                          'data4':data4,'data5':data5,
                                          'data6':data6})
    
    
def condition(request):
    data=100
    return render(request,'cond.html',{'data':data})

def home(request,data):
    return render(request,'home.html',{'data':data})


def rep(request):
    data=[['dinga','dinga@gmail.com',99665522,25,'bangalore'],['sai','sai@gmail.com',99665526000,30,'chennai']]
    return render(request,'rep.html',{'data':data})
    