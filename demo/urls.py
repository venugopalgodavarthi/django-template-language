from django.urls import path
from demo import views
urlpatterns=[
    path('dhome/',views.dhome,name="dhome"),
    path('signal/',views.signal,name="signal"),
    ]