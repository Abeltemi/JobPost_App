from django.shortcuts import render, redirect
from django.urls import reverse
from subscribe.models import Subscriber
from subscribe.forms import SubscribeForm
# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST) # binding data to the form
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("form is valid")
            # form = subscribe_form.cleaned_data
            # print(form)
            # email = form['email']            
            # firstname = form['first_name']
            # lastname = form['last_name']
            
            # subscriber = Subscriber(first_name=firstname, email=email, last_name=lastname)
            # subscriber.save()
            return redirect(reverse('thank_you'))
        # firstname = request.POST.get('firstname')
    context = {'form': subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    return render(request, 'subscribe/thankYou.html')