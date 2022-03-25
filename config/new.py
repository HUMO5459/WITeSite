from django.urls import path
from django.views import DemoListView, DemoListView2, DemoListView3, DemoListView4, DemoListView5, DemoListView6

urlpatterns = [
    path('', DemoListView.as_view(), name='home'),
    path('about/', DemoListView2.as_view(), name='about'),
    path('services/', DemoListView3.as_view(), name='services'),
    path('projects/', DemoListView4.as_view(), name='projects'),
    path('contact/', DemoListView5.as_view(), name='contact'),
    path('learn/', DemoListView6.as_view(), name='learn')
]