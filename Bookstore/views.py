from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Books,Register
from .models import Login


def home(request):
    if 'uname' in request.session:
        data = Books.objects.all()
        return render(request,template_name='homebook.html',context={'data':data})

    else:
        return redirect('login')
    return render(request,'login.html')

def addbook(request):
    if request.method == "POST":
        book_obj = Books()
        book_obj.book_name = request.POST.get('bname')
        book_obj.book_author = request.POST.get('bauthor')
        book_obj.book_price = request.POST.get('bprice')
        book_obj.book_image = request.POST.get('bimage')
        book_obj.book_details = request.POST.get('description')
        book_obj.save()
        return redirect('/home/')
    return render(request, 'addbook.html')



def delete(request, id):
    book_obj = Books.objects.get(id=id)
    book_obj.delete()
    return redirect(('/home/'))


def update(request, id):
    book_obj = Books.objects.get(id=id)
    print("book_obj")
    if request.method == "POST":
        book_obj = Books.objects.get(id=id)

        book_obj.book_name = request.POST.get('bname')
        book_obj.book_author = request.POST.get('bauthor')
        book_obj.book_price = request.POST.get('bprice')
        book_obj.book_image = request.POST.get('bimage')
        book_obj.book_details = request.POST.get('description')
        book_obj.save()
        return redirect('/home/')
    return render(request, 'updatebook.html', {'data': book_obj})




def login(request):
    if request.method == "POST":
        user_name = request.POST.get('uname')
        user_pwd = request.POST.get('upass')
        user = Register.objects.filter(user_name=user_name,user_pwd=user_pwd).first()
        if user:
            request.session['uname'] = user_name
            return redirect('/home/')
        else:
            return render(request,template_name='login.html',context={'error':'Invalid username or password'})
    return render(request,template_name='login.html')

def register(request):
    if request.method=='POST':
        user_obj = Register()
        user_obj.full_name = request.POST.get('fullname')
        user_obj.user_name = request.POST.get('uname')
        user_obj.user_pwd = request.POST.get('upass')
        user_obj.user_id = request.POST.get('email')
        user_obj.save()
        return redirect('/login/')
    return render(request, 'register.html')

def logout(request):
    logout(request)
    return redirect('/login')

# Create your views here.
