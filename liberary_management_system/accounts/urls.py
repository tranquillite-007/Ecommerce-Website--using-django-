# accounts/urls.py
from django.urls import path
from .views import custom_logout_view
from .views import dashboard_view, maintenance_view, report_view, transaction_view, login_view, home_view, user_dashboard, admin_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('dashboard/user/', user_dashboard, name='user_dashboard'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),  
    path('maintenance/', maintenance_view, name='Maintenance'),
    path('report/', report_view, name='Report'),
    path('transaction/', transaction_view, name='Transaction'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', custom_logout_view, name='logout'),  # Use your custom logout view
]