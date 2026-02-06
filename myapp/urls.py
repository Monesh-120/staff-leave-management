from django.urls import path
from .views import login_view,register_view,admin_dashboard,user_dashboard,logout_view,home,manage_staff,add_staff,delete_staff,edit_staff


urlpatterns=[
    path('',home,name='home'),
	path('login/',login_view,name='login'),
	path('register/',register_view,name='register'),
    path('admin-dashboard/',admin_dashboard,name='admin_dashboard'),
    path('user-dashboard/',user_dashboard,name='user_dashboard'),
    path('logout-view/',logout_view,name='logout'),
    # path('admin-leave-management/',admin_leave_management,name='admin_leave_management'),
    # path('leave-approval/',leave_approval,name='leave_approval'),
    path('manage_staff/',manage_staff,name='manage_staff'),
    path('add-staff/',add_staff,name='add_staff'),
    path('delete-staff/<int:id>',delete_staff,name='delete_staff'),
    path('edit-staff/<int:id>',edit_staff,name='edit_staff'),
]