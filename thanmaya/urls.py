"""thanmaya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('blog.urls'))

]"""
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_view
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static


 
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('Login/', blog_view.Login, name ='Login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('Register/', blog_view.register, name ='Register'),
    path('slideshow/', blog_view.slideshow, name='slideshow'),
     path('home/', blog_view.home, name='home'),
     path('post/', blog_view.post, name='post'),
     path('contact/', blog_view.contact, name='contact'),
     path('postindex/', blog_view.post_index, name='postindex'),
     path("post/<int:pk>/", blog_view.blog_detail, name="blog_detail"),
     path("category/<category>/", blog_view.blog_category, name="blog_category"),
     

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


