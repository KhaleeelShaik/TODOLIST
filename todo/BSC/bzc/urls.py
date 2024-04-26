from django. urls import path
from .import views

urlpatterns = [
    path("",views.fun,name='fun'),
    path("signup/",views.signup,name='signup'),
    path("signin/",views.signin,name='signin'),
    path('display/',views.display,name='display'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('search/',views.search,name='search'),
    path('finish/<int:id>',views.finish,name='finish'),
   
 ]
