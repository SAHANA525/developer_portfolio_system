#s1/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect 
from .models import Admin,Skill,Project,Student,Eduction,Intrests,Experience
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

  
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
   
def home(request): 
    return render(request, 'home.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')



def admin1(request):
    username = "admin"
    password = "admin5"
    #member = Admin.objects.all().values()
    if username=="admin" and password=="admin5":
      return render(request, "main.html")
    else:
      return render(request, "admin.html")





def adminlogin(request): 
  return render(request, 'admin.html')
    #return render(request, 'adminprofile.html')

def resume(request):
  mymembers = Student.objects.all().values()
  mymembers1 = Eduction.objects.all().values()
  mymembers2 = Skill.objects.all().values()
  mymembers3 = Experience.objects.all().values()
  mymembers4 = Project.objects.all().values()
  mymembers5 = Intrests.objects.all().values()
  template = loader.get_template('resume.html')
  context = {
    'mymembers': mymembers,
    'mymembers1': mymembers1,
    'mymembers2': mymembers2,
    'mymembers3': mymembers3,
    'mymembers4': mymembers4,
    'mymembers5': mymembers5,

  }
  return HttpResponse(template.render(context, request))
  



    
    
def main(request): 
    return render(request, 'main.html')
   
def signout(request):
    logout(request)
    return redirect('/profile')

#################################skills model
def saveskill(req):
    if req.method=="POST":
        #print("this is post example!")
        if req.POST.get('skill') and req.POST.get('description'):
            saverecord=Skill()
            saverecord.skill=req.POST.get('skill')
            saverecord.description=req.POST.get('description')
            #print(name,email,contact,comment)
            saverecord.save()
            messages.success(req,'recored saved')
            return redirect('/index')
    else:
        return render(req,'saveskill.html')


def index(request):
  mymembers = Skill.objects.all().values()
  template = loader.get_template('deleteskill.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def deleteskill(request,id):
  member = Skill.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Skill.objects.get(id=id)
  template = loader.get_template('updateskill.html')
  context = {
    'mymember': mymember,
  }

  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  skill = request.POST['skill']
  description = request.POST['description']
  member = Skill.objects.get(id=id)
  member.skill = skill
  member.description = description
  member.save()
  return HttpResponseRedirect(reverse('index'))

###########################project Model
def saveproject(req):
    if req.method=="POST":
        #print("this is post example!")
        if req.POST.get('project') and req.POST.get('description'):
            saverecord=Project()
            saverecord.project=req.POST.get('project')
            saverecord.description=req.POST.get('description')
            #print(name,email,contact,comment)
            saverecord.save()
            messages.success(req,'recored saved')
            return redirect('/indexproject')
    else:
        return render(req,'saveproject.html')


def indexproject(request):
  mymembers = Project.objects.all().values()
  template = loader.get_template('deleteproject.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def deleteproject(request,id):
  member = Project.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('indexproject'))

def updateproject(request, id):
  mymember = Project.objects.get(id=id)
  template = loader.get_template('updateproject.html')
  context = {
    'mymember': mymember,
  }

  return HttpResponse(template.render(context, request))

def updaterecordproject(request, id):
  project = request.POST['project']
  description = request.POST['description']
  member = Project.objects.get(id=id)
  member.project = project
  member.description = description
  member.save()
  return HttpResponseRedirect(reverse('indexproject'))

  ########################### student Model
def indexstudent(request):
  mymembers = Student.objects.all().values()
  template = loader.get_template('deletestudent.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def updatestudent(request, id):
  mymember = Student.objects.get(id=id)
  template = loader.get_template('updatestudent.html')
  context = {
    'mymember': mymember,
  }

  return HttpResponse(template.render(context, request))

def updaterecordstudent(request, id):
  phone= request.POST['phone']
  email= request.POST['email']
  title= request.POST['title']
  role= request.POST['role']
  fname= request.POST['fname']
  lname= request.POST['lname']
  member = Student.objects.get(id=id)
  member.phone = phone
  member.email = email
  member.title = title
  member.role = role
  member.fname = fname
  member.lname = lname
  member.save()
  return HttpResponseRedirect(reverse('indexstudent'))

  ########################### Education Model 

def saveeduction(req):
    if req.method=="POST":
        #print("this is post example!")
        if req.POST.get('degree') and req.POST.get('specialization') and req.POST.get('university') and req.POST.get('school') and req.POST.get('yop') and req.POST.get('per'):
            saverecord=Eduction()
            saverecord.degree=req.POST.get('degree')
            saverecord.specialization=req.POST.get('specialization')
            saverecord.university=req.POST.get('university')
            saverecord.school=req.POST.get('school')
            saverecord.yop=req.POST.get('yop')
            saverecord.per=req.POST.get('per')
            #print(name,email,contact,comment)
            saverecord.save()
            messages.success(req,'recored saved')
            return redirect('/indexeduction')
    else:
        return render(req,'saveeduction.html')


def indexeduction(request):
  mymembers = Eduction.objects.all().values()
  template = loader.get_template('deleteeduction.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def deleteeduction(request,id):
  member = Eduction.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('indexeduction'))

def updateeduction(request, id):
  mymember = Eduction.objects.get(id=id)
  template = loader.get_template('updateeduction.html')
  context = {
    'mymember': mymember,
  }

  return HttpResponse(template.render(context, request))

def updaterecordeduction(request, id):
  degree= request.POST['degree']
  specialization= request.POST['specialization']
  university= request.POST['university']
  school= request.POST['school']
  yop= request.POST['yop']
  per= request.POST['per']
  member = Eduction.objects.get(id=id)
  member.degree = degree
  member.specialization = specialization
  member.university = university
  member.school = school
  member.yop = yop
  member.per = per
  member.save()
  return HttpResponseRedirect(reverse('indexeduction'))

  ########################### Experience Model 

def saveexp(req):
    if req.method=="POST":
        #print("this is post example!")
        if req.POST.get('company') and req.POST.get('role') and req.POST.get('nyear') and req.POST.get('description'):
            saverecord=Experience()
            saverecord.company=req.POST.get('company')
            saverecord.role=req.POST.get('role')
            saverecord.nyear=req.POST.get('nyear')
            saverecord.description=req.POST.get('description')
            #print(name,email,contact,comment)
            saverecord.save()
            messages.success(req,'recored saved')
            return redirect('/indexexp')
    else:
        return render(req,'saveexp.html')


def indexexp(request):
  mymembers = Experience.objects.all().values()
  template = loader.get_template('deleteexp.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def deleteexp(request,id):
  member = Experience.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('indexexp'))

def updateexp(request, id):
  mymember = Experience.objects.get(id=id)
  template = loader.get_template('updateexp.html')
  context = {
    'mymember': mymember,
  }

  return HttpResponse(template.render(context, request))

def updaterecordexp(request, id):
  company= request.POST['company']
  role= request.POST['role']
  nyear= request.POST['nyear']
  description= request.POST['description']
  member = Experience.objects.get(id=id)
  member.company= company
  member.role = role
  member.nyear = nyear
  member.description= description
  member.save()
  return HttpResponseRedirect(reverse('indexexp'))

#################################Intrests model
def saveintr(req):
    if req.method=="POST":
        #print("this is post example!")
        if req.POST.get('links') and req.POST.get('hobies'):
            saverecord=Intrests()
            saverecord.links=req.POST.get('links')
            saverecord.hobies=req.POST.get('hobies')
            #print(name,email,contact,comment)
            saverecord.save()
            messages.success(req,'recored saved')
            return redirect('/indexintr')
    else:
        return render(req,'saveintr.html')


def indexintr(request):
  mymembers = Intrests.objects.all().values()
  template = loader.get_template('deleteintr.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def deleteintr(request,id):
  member = Intrests.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('indexintr'))

def updateintr(request, id):
  mymember = Intrests.objects.get(id=id)
  template = loader.get_template('updateintr.html')
  context = {
    'mymember': mymember,
  }

  return HttpResponse(template.render(context, request))

def updaterecordintr(request, id):
  links = request.POST['links']
  hobies = request.POST['hobies']
  member = Intrests.objects.get(id=id)
  member.links = links
  member.hobies = hobies
  member.save()
  return HttpResponseRedirect(reverse('indexintr'))
