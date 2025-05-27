#定义accounts应用的URL路由
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # 包含默认的身份验证 URL
    path('', include('django.contrib.auth.urls')),  # 包含Django内置的身份验证URL
    # 注册新用户的URL
    path('register/', views.register, name='register'),  # 用户注册视图
]