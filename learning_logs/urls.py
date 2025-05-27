"""定义lesrning_logs的URL模式"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    #显示所有主题的页面
    path('topics/', views.topics, name='topics'),
    #特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #添加主题
    path('new_topic/', views.new_topic, name='new_topic'),
    #添加笔记
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #编辑笔记
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #编辑主题
    path('edit_topic/<int:topic_id>', views.edit_topic, name='edit_topic')
]