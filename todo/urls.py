from django.urls import path
from .views import ListTodo,TodoCreateView,TodoDeleteView,TodoUpdateView
from . import views
app_name='todo'
urlpatterns = [
    path('home/<int:user_id>/', ListTodo.as_view(),name='home'),
    path('new/', TodoCreateView.as_view(), name="create"),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name="update"),
    path('cross/<int:obj_id>/',views.cross_off,name='cross'),
    path('uncross/<int:obj_id>/',views.uncross,name='uncross'),
]