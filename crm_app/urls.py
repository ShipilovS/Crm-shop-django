from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name='home_page'),
    path('order/<str:slug>/<int:id_order>', make_order, name='make_order'),
    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='registration'),
    path('loguot/', logout_user, name='loguot'),
    path('u<int:id_profile>/', profile_page, name='profile'),
    path('u<int:id_profile>/<int:id_order>/', make_process, name='make_process'),
    path('delete<int:id_order>/', delete_order, name='delete_order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)