from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')
