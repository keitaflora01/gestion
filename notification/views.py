from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Rappel
# Create your views here.
   
def feedback(request):
    user = request.user  # Assuming you have a Profile model linked to User
    message = Rappel.objects.filter(user=user).order_by('-date')  # Fetch messages for the user
    if request.method == 'POST':
        message = request.POST.get('content', '')
        title = request.POST.get('message_type','Message')
        if message:
            Rappel.objects.create(
                user=user, 
                title=title, 
                message=message,
                date = timezone.now()
            )
            return redirect('feedback')  # Redirect to a success page or back to the dashboard
        else:
    
            return render(request, 'tableaubord/feedback.html', {
                'erreur': 'le message est obligatoir',
                'messages': message})  # Redirect to a success page or back to the dashboard
    
    return render(request, 'tableaubord/feedback.html',{'messages':message})  # Render the support page with the form