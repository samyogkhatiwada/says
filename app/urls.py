from django.urls import path
from . import views
# link static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('<str:username>', views.addConfession, name='addConfession'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)