from django.urls import path

from . import views

app_name = 'scan'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('scan/', views.scan, name='scan'),
    path('scan/<int:pk>', views.scan, name='scan'),
    path('<slug:qrcode>/mark', views.mark, name='mark'),
    path('create/', views.SubscriptionCreate.as_view(), name='subscription_create'),
    path('<int:pk>/update/', views.SubscriptionUpdate.as_view(), name='subscription_update'),
    path('<int:pk>/delete/', views.SubscriptionDelete.as_view(), name='subscription_delete'),
    path('report', views.visitreport, name='report')
]

