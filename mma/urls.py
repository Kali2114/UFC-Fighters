from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from UFC.views import my_logout
from UFC.api import UserView, FighterView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'fighter', FighterView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ufc/', include('UFC.urls')),
    path('login/', auth_views.LoginView.as_view(next_page='fighters'), name='login'),
    path('logout/', my_logout, name='my_logout'),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
