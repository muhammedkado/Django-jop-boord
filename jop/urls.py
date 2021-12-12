
from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.Jop_list),
    path('<int:id>',views.Jop_detail)
]