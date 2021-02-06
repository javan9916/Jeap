from django.shortcuts import render

####### global variables #################
styles_home = 'styles/home.css'         ##
styles_projects = 'styles/projects.css' ##
styles_plans = 'styles/plans.css'       ##
styles_about = 'styles/about.css'       ##
##########################################

def home(request):
    context = {
        'home_page': 'active',
        'styles': styles_home,
    }
    return render(request, 'home.html', context)

def projects(request):
    context = {
        'project_page': 'active',
        'styles': styles_projects
    }
    return render(request, 'projects.html', context)
    
def plans(request):
    context = {
        'plan_page': 'active',
        'styles': styles_plans
    }
    return render(request, 'plans.html', context)
        
def about(request):
    context = {
        'about_page': 'active',
        'styles': styles_about
    }
    return render(request, 'about.html', context)
    