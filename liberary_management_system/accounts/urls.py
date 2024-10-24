# accounts/urls.py
from django.urls import path
from .views import maintenance_view, report_view, transaction_view, login_view, home_view, user_dashboard, admin_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('dashboard/user/', user_dashboard, name='user_dashboard'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),  # Custom admin dashboard
    path('maintenance/', maintenance_view, name='Maintenance'),
    path('report/', report_view, name='Report'),
    path('transaction/', transaction_view, name='Transaction'),

]