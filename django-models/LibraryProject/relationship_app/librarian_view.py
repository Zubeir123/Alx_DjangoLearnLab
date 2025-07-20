from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')
