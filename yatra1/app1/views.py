from django.shortcuts import render, HttpResponse
from app1.models import student
from app1.models import user
# from contactenquiry.models import contactEnquiry

# Create your views here.
def home(request):
    return render(request,"home.html")
def home2(request):
    return render(request,"home2.html")


def contact(request):
    return render(request,"contact.html")
# def saveEnquiry(request):
#     if request.method=="POST":
#         name=request.POST.get["name"]
#         email=request.POST.get["email"]
#         msg=request.POST.get["msg_box"]
#         print(name,email,msg)
#         enquiry=contactEnquiry(name=name,email=email,msg_box=msg)
#         enquiry.save()
#     return HttpResponse("submited successfully")




def regis(request):
    return render(request,"regis.html")
def login(request):
    return render(request,"login.html")
def signin(request):
    return render(request,"signin.html")

def goahony(request):
    return render(request,"goahony.html")
def kerhony(request):
    return render(request,"kerhony.html")
def simhony(request):
    return render(request,"simhony.html")
def mussorie(request):
    return render(request,"mussorie.html")
def goa(request):
    return render(request,"goa.html")
def manali(request):
    return render(request,"manali.html")
def vashno(request):
    return render(request,"vashno.html")
def andaman(request):
    return render(request,"andaman.html")
def nanital(request):
    return render(request,"nanital.html")


def tamil(request):
    return render(request,"tamil.html")

def orrisa(request):
    return render(request,"orrisa.html")
def assam(request):
    return render(request,"assam.html")
def agra(request):
    return render(request,"agra.html")
def kashmir(request):
    return render(request,"kashmir.html")
def tourkasm(request):
    return render(request,"tourkasm.html")
def packagekasm(request):
    return render(request,"packagekasm.html")
def dayskasm(request):
    return render(request,"dayskasm.html")
def specialkasm(request):
    return render(request,"specialkasm.html")
def devikasmir(request):
    return render(request,"devikasmir.html")
def mastourpak(request):
    return render(request,"mastourpak.html")
def kastourpak(request):
    return render(request,"kastourpak.html")
def jaitourpak(request):
    return render(request,"jaitourpak.html")
def udapur(request):
    return render(request,"udapur.html")
def guwwild(request):
    return render(request,"guwwild.html")
def ladkh(request):
    return render(request,"ladkh.html")
def jaipurwild(request):
    return render(request,"jaipurwild.html")
def sundarbanwild(request):
    return render(request,"sundarbanwild.html")
def popularand(request):
    return render(request,"popularand.html")
def popularnainital(request):
    return render(request,"popularnainital.html")
def chardham(request):
    return render(request,"chardham.html")
def index(request):
    return render(request,"index.html")
def spinwheel(request):
    return render(request,"spinwheel.html")
def myjrny(request):
    return render(request,"myjrny.html")
def newjrny(request):
    return render(request,"newjrny.html")
def nav(request):
    return render(request,"nav.html")
def demo(request):
    return render(request,"demo.html")
def wildlife(request):
    return render(request,"wildlife.html")



def saveform(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        gender=request.POST["gender"]
        seating=request.POST["seating"]
        diet=request.POST["diet"]
        handicap=request.POST["handicap"]
        address=request.POST["address"]
        country=request.POST["country"]
        print(name,email,phone,gender,seating,diet,handicap,address,country)
        my_model=student(st_name=name,st_email=email,st_phone=phone,st_gender=gender,st_seating=seating,st_diet=diet,st_handicap=handicap,st_address=address,st_country=country)
        my_model.save()
    return HttpResponse("submited successfully")


def res(request):
    data = student.objects.all()
    con={'Std':data}
    return render(request, 'res.html',con)

def savepoint(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        
        print(name,email,password,)
        my_model=user(st_name=name,st_email=email,st_password=password)
        my_model.save()
    return HttpResponse("submited successfully")


def search(request):
    query = request.GET['query']
    allstudent = student.objects.all()
    allstudent = student.objects.filter(st_name__icontains=query)
    params = {
        'allstudent': allstudent
    }



    return render(request, 'search.html', params)
    # return HttpResponse('this is search')