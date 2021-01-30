from django.shortcuts import render

####### global variables #########
style = 'styles/styles.css'     ##
##################################

def home(request):
    context = {
        'home_page': 'active',
        'styles': style,
    }
    return render(request, 'home.html', context)

def projects(request):
    context = {
        
    }
    return render(request, 'projects.html', context)