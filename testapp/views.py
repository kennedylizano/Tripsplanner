from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")


def Createuser(request):
    print(request.POST)
    errorValidor = User.objects.userValidor(request.POST)
    if len(errorValidor) > 0:
        for key, value in errorValidor . items ():
            messages.error(request, value)
        return redirect("/")
    else:
        ashpassword = bcrypt.hashpw(request.POST["pw"].encode(),bcrypt.gensalt()).decode()
        usercreate = User.objects.create(name=request.POST["name"],username = request.POST["username"], password= ashpassword)
        print(usercreate)
        request.session["userID"] = usercreate.id
    return redirect("/travels")

def travels(request,):
    user=User.objects.get(id=request.session["userID"])
    context = {
        "user":user,
         "loggeuser":Trip.objects.filter(Q(created_by=user) | Q(participants=user)),
         "differenttrips" : Trip.objects.exclude(Q(created_by=user) | Q(participants=user)),
         "trips":Trip.objects.all(),}
    return render(request,"travel.html", context)

def Login(request):
    print(request.POST)
    errorValidor = User.objects.logindvalitor(request.POST)
    if len(errorValidor)>0:
        for key, value in errorValidor. items ():
            messages.error(request, value)
        return redirect("/")
    user =User.objects.get(username= request.POST['username'])
    request.session["userID"]= user.id
    return redirect("/travels")

def addtravel(request):
    return render(request,"addtravel.html")

def addatrip(request):
        print(request.POST)
        errorValidor = Trip.objects.tripValitor(request.POST)
        if len(errorValidor) > 0:
            for key, value in  errorValidor . items ():
                messages.error(request, value)
            return redirect("/travels/add")
        else:
            loggedinuser = User.objects.get(id = request.session["userID"] )
            createatrip = Trip.objects.create(destination = request.POST["Destination"],description = request.POST["description"],startdate = request.POST["startdate"],enddate = request.POST["enddate"],created_by =loggedinuser)
            print(createatrip)
        return redirect("/travels")

def views(request,viewsID):
    context = {
    "viweId":Trip.objects.get(id=viewsID),

     }
    return render(request,"views.html", context)

def join(request,Id):
    loggedinuser = User.objects.get(id = request.session["userID"] )
    context ={
        "user":loggedinuser
    }
    trip = Trip.objects.get(id=Id)
    trip.participants.add(User.objects.get(id=request.session["userID"]))
    return redirect("/travels",context)

def logout(request):
    request.session.clear()
    return redirect("/")
