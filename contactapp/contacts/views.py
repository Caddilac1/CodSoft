from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request , 'home.html')


def add_contact(request):
    if request.method == 'POST':
        # Extract form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        saved_to = request.POST.get('save')
        whatsapp = request.POST.get('whatsapp', False)

        # Since phone is required, it's safe to assume it exists
        if phone.startswith("0"):
            phone = "+233" + phone[1:]
        
        # Determine if 'whatsapp' is selected
        is_whatsapp = True if whatsapp == 'on' else False

        # Save the contact
        contacts = Contact(
            user=request.user,
            fname=fname,
            lname=lname,
            phone=phone,
            email=email,
            saved_to=saved_to,
            is_whatsapp=is_whatsapp
        )
        contacts.save()
        messages.success(request, 'Contact added successfully')
        return redirect('view_contact')
    
    messages.info(request, "Something went wrong")
    return render(request, 'add-contact.html')



def view_contacts(request):
    contacts = Contact.objects.filter(user = request.user)
    total = Contact.objects.filter(user = request.user).count()
    context = {'contacts': contacts , 'total': total}
    return render(request , 'view-contact.html' , context)

def view_details(request , pk):
    contd = Contact.objects.filter(user = request.user ).get(id = pk)
    context = {'contd': contd}
    return render(request , 'contact_details.html' , context)

def edit_contact(request, pk):
    conte = Contact.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        conte.fname = request.POST.get('fname')
        conte.lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        conte.email = request.POST.get('email')
        conte.saved_to = request.POST.get('save')
        if phone.startswith("0"):
            phone = "+233" + phone[1:]
        conte.phone = phone
        conte.is_whatsapp = request.POST.get('whatsapp') == 'on'
        conte.save()
        messages.success(request, 'Contact updated successfully')
        return redirect('view_contact')
    return render(request, 'edit-contact.html', {'conte': conte})




def updatestatus(request,pk):
    stat = Contact.objects.filter(user = request.user).get(id = pk)
    stat.is_whatsapp = not stat.is_whatsapp
    stat.save()
    messages.success(request, 'Todo status updated successfully')
    return redirect('view_todo')



def signup(request):
    return render(request , 'Signup_page.html')


def signin(request):
    return render(request , 'Login-page.html')

def signout(request):
    return redirect('home')
