from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/tools/', views.tools, name='tools'),
    path('categories/seeds/', views.seeds, name='seeds'),
    # path('categories/seedlings/', views.seedlings, name='seedlings'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password, name='fp'), 
    path('create-account/', views.create_account, name='new_account'),
    path('upload/', views.upload_equipment, name='upload_equipment'),
    path('equipment_list/', views.equipment_list, name='equipment_list'),
    path('search/', views.search_equipment, name='search_results'),
    path('rent/<int:equipment_id>/', views.rent_equipment, name='rent_equipment'),
    path('calendar_booking/<int:equipment_id>/', views.calendar_booking, name='calendar_booking'),
    path('payment/<int:equipment_id>/', views.payment_page, name='payment_page'),
    path('payment2/', views.payment2_view, name='payment2_page'),
    path('subscription1/', views.subscription1, name='subscription1'),
    path('subscription2/', views.subscription2, name='subscription2'),
    path('subscription3/', views.subscription3, name='subscription3'),
    path('subscription4/', views.subscription4, name='subscription4'),
]
