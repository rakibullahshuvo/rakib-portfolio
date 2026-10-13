from django.shortcuts import render, redirect
from .models import ContactMessage

def home_view(request):
    return render(request, "index.html")


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            return redirect('/?contact=success')

        return redirect('/?contact=error')

    return redirect('/')
