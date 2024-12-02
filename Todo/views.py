from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.



def home(request):
    return render(request , 'home.html');

@login_required
def add_Todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        Description = request.POST['task']
        due = request.POST['due']

        todo = Todo(user=request.user , title = title , Description = Description , due = due)
        todo.save()
        messages.success(request, f'Todo was added succesfully by {request.user.username}')
        return redirect('/view_todo/')
    return render(request, 'add_todo.html')


@login_required
def view_Todo(request):
    search = request.GET.get('search', '')

    if search:  
        todos = Todo.objects.filter(user=request.user, title__icontains=search)  
        incomplete = Todo.objects.filter(user=request.user, completed=False)
        incomplete_task = incomplete.count()
        context = {'todos': todos, 'incomplete': incomplete, 'incomplete_task': incomplete_task}
    else:
        todos = Todo.objects.filter(user=request.user)
        incomplete = Todo.objects.filter(user=request.user, completed=False)
        incomplete_task = incomplete.count()
        context = {'todos': todos, 'incomplete': incomplete, 'incomplete_task': incomplete_task}

    return render(request, 'view_todo.html', context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 6:
            messages.error(request , 'Your password should not be less than 6 charaters')
            return redirect('signup')
        
        get_usernames = User.objects.filter(username = username)
        get_email = User.objects.filter(email = email)

        if get_usernames:
            messages.error(request , 'Username already exist')
            return redirect('signup')
        
        elif get_email:
            messages.error(request , 'email already exist')
            return redirect('signup')
        
        user = User.objects.create_user(username = username , email = email , password = password)
        user.save()
        messages.success(request, 'Your account has been created successfully!')
        return redirect('loginpage')

    return render(request , 'Signup_page.html')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)

        except User.DoesNotExist:
            messages.info(request , 'Account not found')
            return redirect('loginpage')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            messages.success(request , f'Successfully logged in as {request.user.username}')
            return redirect('view_todo')   
        else:
            messages.error(request, 'Incorrect username or password. Please try again.')
            return redirect('loginpage')
    
    return render(request, 'Login-page.html')


def logoutpage(request):
    logout(request)
    messages.success(request , 'You have been successfully logged out')
    return redirect('home')

@login_required
def updatestatus(request,pk):
    stat = Todo.objects.filter(user = request.user).get(id = pk)
    stat.completed = not stat.completed
    stat.save()
    messages.success(request, 'Todo status updated successfully')
    return redirect('view_todo')

@login_required
def view_todo_details(request,pk):
    details = Todo.objects.filter(user = request.user).get(id=pk)
    context = {'details':details}
    return render(request , 'view_todo_detail.html' , context)

@login_required
def edit_todo(request, pk):
    # Retrieve the todo item based on user and primary key (pk)
    ed = Todo.objects.filter(user=request.user).get(id=pk)

    # Check if the form has been submitted
    if request.method == 'POST':
        # Get form values
        ed.title = request.POST.get('title')
        ed.Description = request.POST.get('description')
        ed.due = request.POST.get('due')
        
        # Check if the completed checkbox is checked, and update the completed status
        ed.completed = 'completed' in request.POST
        
        # Save the updated todo item
        ed.save()

        # Display a success message
        messages.success(request, 'Todo updated successfully')

        # Redirect to the view_todo page
        return redirect('view_todo')
    context = {'ed': ed}

    return render(request, 'edit_todo.html', context)


@login_required
def delete_todo(request,pk):
    de = Todo.objects.filter(user = request.user).get(id=pk)
    de.delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('view_todo')

def contact(request):
    if request.method == 'POST':
        send_via = request.POST.get('send_method')

        
        if send_via == 'email':
            return redirect('email')  
    return render(request, 'contact.html')


def email(request):
    if request.method == 'POST':
        print(request.POST)
        sender = request.POST.get('sender')  # Get the sender's name
        sender_email = request.POST.get('sender_email')  # Get the sender's email
        message = request.POST.get('message')  # Get the feedback message

        try:
            send_mail(
                'Feedback from ' + sender,  # Subject of the email
                message,  # Body of the email
                sender_email,  # From email (using the sender's email)
                ['nabaradirector@gmail.com'],  # To email (your email set in settings)
                fail_silently=False
            )
            print("Email sent successfully!") 
            print(f"Email Details - Subject: Feedback from {sender}, Message: {message}, From: {sender_email}, To: {settings.EMAIL_HOST_USER}")
 # Log success
            return HttpResponse('Feedback sent successfully!')  # Optional: Confirm feedback sent
        except Exception as e:
            print(f"Error: {e}")  # Log the error for debugging
            return HttpResponse(f"Failed to send feedback: {e}")  # Show error in response
    return render(request, 'email.html')
