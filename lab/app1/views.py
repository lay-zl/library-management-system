from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def home(req):
    return render(req,'home.html')

def allbook(req):
    ob = Book.objects.all()
    return render(req,'allbook.html',{'ob':ob})

def login(req):
    msg = ''
    if req.method == 'POST':
        data = req.POST  # firstname lastname phoneno email
        User.objects.create(firstname=data.get('fname'),lastname=data.get('lname'),phoneno=data.get('ph'),email =data.get('email'))
        msg = 'user ad '
        return render(req, 'login.html',{'msg':msg})
    return render(req,'login.html')

def addbook(req):
    msg = ''
    if req.method == 'POST':
        data = req.POST
        bn = data.get('bname')
        p = data.get('pub')
        a = data.get('auth') # name author publisher
        Book.objects.create(name=bn,author = a,publisher=p)
        msg = 'book added..back to home'
        return render(req, 'addbook.html',{'msg':msg})
    return render(req,'addbook.html')

def issuebook(req):
    msg = ''
    if req.method == 'POST':
        data = req.POST
        bid = data.get('bid')
        mid = data.get('mid')
        bn = data.get('bname')
        da = data.get('date')
        rdt = data.get('rdate')
        mn = data.get('mname')
        bo = Book.objects.filter(id=bid).first()
        ur = User.objects.filter(id=mid).first()
        #Issuebook.objects.create(idate=da,user=ur,book=bo)
        Issuebook.objects.create(user=ur, book=bo)
        msg = 'issued book..back to home'
        return render(req, 'issuebook.html',{'msg':msg})
    return render(req,'issuebook.html')
from .f_form import *
def editbook(req,id):
    if req.method=='POST':
        pi = Book.objects.get(id=id)
        ob = EditBookForm(req.POST,instance=pi)
        ob.save()
        return HttpResponseRedirect('/allbook/')
    else:
        pi=Book.objects.get(id=id)
        ob = EditBookForm(instance=pi)
    return render(req,'editbook.html',{'ob':ob})
def allmember(req):
    ob = User.objects.all()
    return render(req,'allmb.html',{'ob':ob})
def allmemberwithbook(req):
    ob = Issuebook.objects.select_related().values('idate','rdate','user__id','user__firstname','user__lastname','user__email','user__phoneno',
                                                   'book__id','book__name')
    return render(req,'allmember.html',{'ob':ob})
def deletebook(req,id):
    ob=Book.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect('/allbook/')
def editmember(req,id):
    if req.method=='POST':
        ob=User.objects.get(id=id)
        f= EditUser(req.POST,instance=ob)
        f.save()
        return HttpResponseRedirect('/allmember/')
    ob=User.objects.get(id=id)
    f = EditUser(instance=ob)
    return render(req,'editmember.html',{'f':f})
def deletemember(req,id):
    ob = User.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect('/allmember/')


def returnbook(req):
    msg = ''
    if req.method=='POST':
        data = req.POST
        mid = data.get('mid')
        bid = data.get('bid')
        u = User.objects.get(id=mid)
        b = Book.objects.get(id=bid)
        ib = Issuebook(user=u,book=b)
        ib.rdate=data.get('rdate')
        ib.save()
        msg = 'return zl..'
        return render(req, 'return.html',{'msg':msg})
    return  render(req,'return.html')
