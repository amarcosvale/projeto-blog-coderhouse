from django.contrib import admin
from django.urls import path, include
from .views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),

    path('pages/', include('pages.urls')),

    # 🔑 AUTENTICAÇÃO
    path('accounts/', include('django.contrib.auth.urls')),
]
