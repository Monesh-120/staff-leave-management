from django.urls import path
from .views import apply_leave,my_leaves,view_leave,approve_leave,reject_leave,admin_leave_management


urlpatterns=[
    path('apply-leave',apply_leave,name='apply_leave'),
    path('my-leaves',my_leaves,name='my_leaves'),
    path('view-leave',view_leave,name='view_leave'),
    path('admin-leave-management',admin_leave_management,name='admin_leave_management'),
    path('approve-leave/<int:id>',approve_leave,name='approve_leave'),
    path('reject-leave/<int:id>',reject_leave,name='reject_leave'),

]