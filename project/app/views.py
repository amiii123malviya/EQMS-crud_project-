from django.shortcuts import render
# from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')


def registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    Cpassword=request.POST.get('Cpassword')
    data=Employee.objects.filter(Email=email)
    print(data)
    if data:
        msg='Already Email Exist'
        return render(request,'register.html',{'key':msg})
    else:
        if password==Cpassword:
            Employee.objects.create(Name=name,
                               Email=email,
                               Password=password)
            msg="Register successfully"
            return render(request,'login.html',{'key':msg})
        
        else:
            msg="password and confirm password not matched"
            return render(request,'register.html',{'key':msg})

def logindata(request):
    # print(request.method)
    print(request.POST)
    email=request.POST.get('email')
    pswrd=request.POST.get('password')
    user=Employee.objects.filter(Email=email)
    if user:
        data=Employee.objects.get(Email=email)
        pss=data.Password
        print(pss)
        print(pswrd)
        if pss == pswrd:
            print(pswrd)
            context={
               'nm':data.Name,
               'em':data.Email,
               'ps':data.Password
            } 
            return render(request,'dashboard.html',{'context':context})
        else:
            msg="Email and Password not matched"
            return render(request,'login.html',{'key':msg})
    else:
        msg="Enter valid EmailId"
        return render(request,'login.html',{'key':msg})
def dashboard(request):
    return render(request,'dashboard.html')
def queryform(request):
    # print(request.POST)
    query=request.POST.get('query')
    discription=request.POST.get('description')
    email=request.POST.get('email')

    Query.objects.create(Query=query,
                             Discriptions=discription,
                             Email=email)
    user1=Employee.objects.get(Email=email)
    context={
               'nm':user1.Name,
               'em':user1.Email,
               'ps':user1.Password
            } 
    data=Query.objects.filter(Email=email)
    return render(request,'dashboard.html',{'key':data,'context':context})
def showdata(request):
    print(request.POST)
    email=request.POST.get('email')
    datas=Query.objects.filter(Email=email)
    if datas:
        user1=Employee.objects.get(Email=email)
        context={
            'nm':user1.Name,
            'em':user1.Email,
            'ps':user1.Password
        }
        all_data=Query.objects.filter(Email=email)
        return render(request,'dashboard.html',{'key1':all_data,'context':context})
    
def delete(request,pk,ml):
    sdel=Query.objects.get(id=pk)
    sdel.delete()
    eml=Query.objects.filter(Email=ml)
    msg="data deleted"
    datas=Query.objects.filter(Email=ml)
    if datas:
            user1=Employee.objects.get(Email=ml)
            context={
               'nm':user1.Name,
               'em':user1.Email,
               'ps':user1.Password
            } 
            all_data=Query.objects.filter(Email=ml)
            return render(request,'dashboard.html',{'key1':all_data,'context':context})

def edit(request,pk):   
    print(request.POST)
    email=request.POST.get('email')
    sedt=Query.objects.get(id=pk)
    
    print("amii",sedt)
    ml=Employee.objects.filter(Email=email)
    msg='data edit'
    if ml:
        user1=Employee.objects.get(Email=email)
        context={
                'nm':user1.Name,
                'em':user1.Email,
                'pass':user1.Password,
                'logout':'logout'
        }
        return render(request,'dashboard.html',{'sedt':sedt,'context':context})

  
def update(request,pk):
    udata=Query.objects.get(id=pk)
    udata.Query=request.POST['query']
    udata.Discriptions=request.POST['description']
    udata.save()
    email=request.POST.get('email')
    ml=Employee.objects.filter(Email=email)
    msg='update data'
    
    if ml:
        udata=Employee.objects.get(Email=email)

        context={
                'nm':udata.Name,
                'em':udata.Email,
                'ps':udata.Password,
                'logout':'logout'
            } 
   
        return render(request,'dashboard.html',{'udata':udata,'context':context})

    



