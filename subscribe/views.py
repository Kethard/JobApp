from django.shortcuts import render

from subscribe.models import Subscribe


# Create your views here.
def subscribe(request):
    email_error_empty= ''
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        same_email = Subscribe.objects.filter(email__iexact=email)
        if email=="":
            email_error_empty="Nie podano adresu email!"
        if same_email:
            email_error_empty = "Podany adres email, znajduje sie juz w naszej bazie"
        else:
            subscribe = Subscribe(first_name = first_name, last_name = last_name, email = email)
            subscribe.save()
    context={'error_email':email_error_empty
    }
    return render(request, 'subscribe/subscribe.html', context)