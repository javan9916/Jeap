from django.shortcuts import render
from .models import VideoItem

####### global variables #################
styles_home = 'styles/home.css'         ##
styles_projects = 'styles/projects.css' ##
styles_video = 'styles/video_detail.css'##
styles_plans = 'styles/plans.css'       ##
styles_about = 'styles/about.css'       ##
carousel = 'js/carousel.js'             ##
##########################################

def home(request):
    context = {
        'home_page': 'active',
        'styles': styles_home,
    }
    return render(request, 'home.html', context)

def projects(request):
    vids = VideoItem.objects.all()

    context = {
        'project_page': 'active',
        'styles': styles_projects,
        'javascript': carousel,
        'video_items': vids
    }
    return render(request, 'projects.html', context)

def video_detail(request, pk):
    vid = VideoItem.objects.get(pk=pk)
    context = {
        'video_item': vid,
        'styles': styles_video
    }
    return render(request, 'video_detail.html', context)
    
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
    