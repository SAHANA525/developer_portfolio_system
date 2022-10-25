
from django.contrib import admin
from django.urls import path
from s1 import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('resume/',views.resume, name='resume'),
    path('admin1/',views.admin1, name='admin1'),
    path('adminlogin/',views.adminlogin, name='adminlogin'),
    path('saveskill/',views.saveskill, name='saveskill'),
    path('deleteskill/<int:id>', views.deleteskill, name='deleteskill'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('index', views.index, name='index'),
        path('saveproject/',views.saveproject, name='saveproject'),
        path('deleteproject/<int:id>', views.deleteproject, name='deleteproject'),
        path('updateproject/<int:id>', views.updateproject, name='updateproject'),
        path('updateproject/updaterecordproject/<int:id>', views.updaterecordproject, name='updaterecordproject'),
        path('indexproject', views.indexproject, name='indexproject'),
    path('updatestudent/<int:id>', views.updatestudent, name='updatestudent'),
    path('updatestudent/updaterecordstudent/<int:id>', views.updaterecordstudent, name='updaterecordstudent'),
    path('indexstudent', views.indexstudent, name='indexstudent'),
        path('saveeduction/',views.saveeduction, name='saveeduction'),
        path('deleteeduction/<int:id>', views.deleteeduction, name='deleteeduction'),
        path('updateeduction/<int:id>', views.updateeduction, name='updateeduction'),
        path('updateeduction/updaterecordeduction/<int:id>', views.updaterecordeduction, name='updaterecordeduction'),
        path('indexeduction', views.indexeduction, name='indexeduction'),
    path('saveexp/',views.saveexp, name='saveexp'),
    path('deleteexp/<int:id>', views.deleteexp, name='deleteexp'),
    path('updateexp/<int:id>', views.updateexp, name='updateexp'),
    path('updateexp/updaterecordexp/<int:id>', views.updaterecordexp, name='updaterecordexp'),
    path('indexexp', views.indexexp, name='indexexp'),

    path('saveintr/',views.saveintr, name='saveintr'),
    path('deleteintr/<int:id>', views.deleteintr, name='deleteintr'),
    path('updateintr/<int:id>', views.updateintr, name='updateintr'),
    path('updateintr/updaterecordintr/<int:id>', views.updaterecordintr, name='updaterecordintr'),
    path('indexintr', views.indexintr, name='indexintr'),

    path('main/',views.main, name='main'),
]
