from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),   
     
    path('logout/', 
         auth_views.LogoutView.as_view(), 
         # auth_views.LogoutView.as_view(next_page=reverse_lazy('memories:index')), 
         name='logout'),
    
    path('', include('memories.urls')),
]
