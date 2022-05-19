from django.contrib import admin
from django.urls import path
from main_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('post/<int:post_id>', views.post_page),
]