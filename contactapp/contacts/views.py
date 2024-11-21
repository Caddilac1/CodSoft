from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request , 'home.html')


def add_contact(request):
    if request.method == 'POST':
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        saved_to = request.POST.get('save')
        whatsapp = request.POST.get('whatsapp', False)

        
        if phone.startswith("0"):
            phone = "+233" + phone[1:]
        
        
        is_whatsapp = True if whatsapp == 'on' else False

       
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



def delete(request , pk):
    de = Contact.objects.filter(request = request.user).get(id = pk)
    de.delete()
    messages.success(request , 'Contact deleted successfully')
    return redirect('view_contact')




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if password < 6:
            messages.error(request , 'Your cannot be less than 6  character')
            return redirect('signup')
        
        get_username = User.objects.filter(username = username)
        get_email = User.objects.filter(email = email)
        

        if get_username:
            messages.info(request , 'Username already exist')
            return redirect('signup')

        elif get_email:
            messages.info(request , 'Email already exist')  
            return redirect('signup')  
        
        user = User.objects.create_user(username = username , email = email , password = password)
        user.save()
        messages.success(request, 'Your account has been created successfully!')
        return redirect('signin')
    return render(request , 'Signup_page.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            messages.info('Account not found') 
            return redirect('signin')

        user = authenticate(request , username = username , password = password)   
        if user is not None:
            login(request, user)
            messages.success(request , f'You have succesfully logged in as {request.user.username}')
            return redirect('view_contact')
        
        else:
            messages.error(request , 'Incorrect username or password... Try again')
            return redirect('signin')
    return render(request , 'Login-page.html')

def signout(request):
    logout(request)
    messages.success(request , 'You have been successfully logged out')
    return redirect('home')
