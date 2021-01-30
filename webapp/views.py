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
        'project_page': 'active',
        'styles': style
    }
    return render(request, 'projects.html', context)
    
def plans(request):
    context = {
        'plan_page': 'active',
        'styles': style
    }
    return render(request, 'plans.html', context)
        
def about(request):
    context = {
        'about_page': 'active',
        'styles': style
    }
    return render(request, 'about.html', context)
    