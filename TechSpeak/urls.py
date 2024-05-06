"""TechSpeak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base.Routes.views import home, about, contact, services
from django.conf.urls.static import static
from TechSpeak import settings
from base.Routes import NoCodeViews, BlogViews, AI_Functions, bot

urlpatterns = []


def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets


# Paths.............................

NoCodeMaker = [
    path('view_pages', NoCodeViews.index, name='view_pages'),
    path('add', NoCodeViews.addPage, name="addpage"),
    path('edit/<id>', NoCodeViews.editPage, name="editpage"),
    path('page/create', NoCodeViews.savePage, name="create_page"),
    path('editPage/<id>', NoCodeViews.editPageContent, name="editPageContent"),
    path('preview/<id>', NoCodeViews.previewPage, name='previewPage')
]

BlogBuilder = [
    path('list_blog', BlogViews.list_blog,name="list_blog"),
    path('list_edit_blog', BlogViews.list_edit_blog,name="list_edit_blog"),
    path('view_blog/<str:pk>', BlogViews.view_blog),
    path('edit_blog/<str:pk>', BlogViews.edit_blog),
    path('blog_edit', BlogViews.blog_edit,name="blog_edit"),
    path('save_blog', BlogViews.save_blog),
    path('delete_blog', BlogViews.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>', BlogViews.save_edit_blog),
]

AI_functions = [
    path('Code_scriping', AI_Functions.Code_scriping,name="Code_scriping"),
    path('Error_Solver', AI_Functions.Error_Solver,name="Error_Solver"),
    path('autogenerate', NoCodeViews.autogenerate, name='autogenerate'),
]



base = [
    path('admin/', admin.site.urls),
    path('url', NoCodeViews.url, name='url'),
    path('Download_file', NoCodeViews.Download_file, name='Download_file'),
    
    path('', home,name='home'),
    path('about', about,name='about'),
    path('contact', contact,name='contact'),
    path('services', services,name='services'),
    
    path('chatbot_res',bot.chatbot_res,name="chatbot_res"),
    
    path('gethtml',NoCodeViews.HTML_Edit,name="gethtml"),
    path('autogenerate_edit',NoCodeViews.autogenerate_edit,name="autogenerate_edit"),
    
]

urlpatterns.extend(Make_Join([NoCodeMaker, BlogBuilder, AI_functions,base]))

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
