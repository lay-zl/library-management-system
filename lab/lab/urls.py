
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('allbook/',allbook,name='allbook'),
    path('login/',login,name='login'),
    path('addbook/',addbook,name='addbook'),
    path('ibook/',issuebook,name='ibook'),
    path('allmember/',allmember,name='allus'),
    path('allmemberwithbook/',allmemberwithbook,name='allmemberbook'),
    path('editbook/<int:id>/',editbook,name='editbook'),
    path('deletebook/<int:id>/',deletebook,name='deletebook'),
    path('editmember/<int:id>/',editmember,name='editmember'),
    path('deletemember/<int:id>/',deletemember,name='deletemember'),
    path('return/',returnbook,name='return')

]
