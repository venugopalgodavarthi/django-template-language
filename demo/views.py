from django.shortcuts import render

# Create your views here.

def dhome(request):
    data ="helloworld"
    return render(request,'dhome.html',{'data':data})

def signal(request):
    data='BLUE'
    lst=[['pys','bang','python development',9966206473],['QSP','bang','java testing',9966206473]]
    return render(request,'dhome.html',{'data':data,'li':lst})