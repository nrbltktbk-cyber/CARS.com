from django.shortcuts import redirect, render
from .forms import ITForm
from .models import ITSecialist

def register_candidate(request):
    if request.method == 'POST':
        form = ITForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = ITForm()
    return render(request, 'register.html', {'form': form}) 

def candidate_list(request):
    candidates = ITSecialist.objects.all()
    return render(request, 'list.html', {'candidates': candidates})

