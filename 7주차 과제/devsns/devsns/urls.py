"""devsns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from snsapp import views

urlpatterns = [
    #메인 경로 index.html
    path('', views.home, name="home"),
    #post table 경로 table.html
    path('posttable/', views.posttable, name="posttable"),
    #post create 경로
    path('postcreate/', views.postcreate, name="postcreate"),
    #게시글 상세 경로
    path('postdetail/<int:post_id>', views.postdetail, name="postdetail"),
    #comment 생성 경로
    path('commentcreate/<int:post_id>', views.commentcreate, name="commentcreate"),
    path('admin/', admin.site.urls),
]
