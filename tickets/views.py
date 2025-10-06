from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm
from .models import Ticket
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Ticket

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tickets:list')
    else:
        form = SignUpForm()
    return render(request, 'tickets/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'tickets/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'tickets:list'

def tickets_list(request):
    q_origin = request.GET.get('origin','').strip()
    q_dest = request.GET.get('destination','').strip()
    qs = Ticket.objects.all().order_by('depart_date')
    if q_origin or q_dest:
        qs = qs.filter(
            Q(origin__icontains=q_origin) & Q(destination__icontains=q_dest)
            if q_origin and q_dest else
            (Q(origin__icontains=q_origin) | Q(destination__icontains=q_dest))
        )
    return render(request, 'tickets/list.html', {'tickets': qs})


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/tickets_detail.html', {'ticket': ticket})