from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Post import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', views.PostView)
router.register('comment', views.CommentView)

urlpatterns = [
    path('', include('Post.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
