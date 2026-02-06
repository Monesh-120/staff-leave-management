from django.shortcuts import render,redirect,get_object_or_404
from .models import Leave
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def apply_leave(request):
    if request.method=='POST':
        Leave.objects.create(
            user=request.user,
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],  
            reason=request.POST['reason'],
            status='Pending'
        )
        return redirect('user_dashboard')
    return render(request, 'leave/apply_form.html')

@login_required
def my_leaves(request):
    leaves = Leave.objects.filter(user=request.user)
    return render(request, 'leave/view_leave.html', {'leaves': leaves})

@login_required
def view_leave(request):
    if request.user.profile.role!='admin':
        return redirect('staff_dashboard')
    leaves=Leave.objects.all()
    return render(request,'leave/leave_approval.html',{'leaves':leaves})

@login_required
def admin_leave_management(request):
    pending=approved=rejected=countofall=0
    # approved=0
    # rejected=0
    # countofall=0
    if request.user.profile.role!='admin':
        return redirect('staff_dashboard')
    leaves=Leave.objects.all()
    for leave in leaves:
        if leave.status=='Pending':
            pending+=1
        elif leave.status=='Approved':
            approved+=1
        elif leave.status=='Rejected':
            rejected+=1
    for leave in leaves:
        countofall+=1
    return render(request,'leave/admin_LM.html',{'leaves':leaves,'pending':pending,'approved':approved,'rejected':rejected,'count_':countofall})

@login_required
def approve_leave(request,id):
    if request.user.profile.role!='admin':
        return redirect('staff_dashboard')
    leave=get_object_or_404(Leave,id=id)
    leave.status='Approved'
    leave.save()
    return redirect('view_leave')

@login_required
def reject_leave(request,id):
    if request.user.profile.role!='admin':
        return redirect('staff_dashboard')
    leave=get_object_or_404(Leave,id=id)
    leave.status='Rejected'
    leave.save()
    return redirect('view_leave')