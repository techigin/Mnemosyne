from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='trans_list'),
    path('<int:id>/transaction/', views.TransactionDeleteView.as_view(), name='tran_del'),
    path('legend/', views.LegendCodeListView.as_view(), name='legend_code_list'),
    path('<int:id>/legend/', views.LegendCodeDeleteView.as_view(), name='code_del'),
]
