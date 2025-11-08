from django.shortcuts import redirect
from django.http import JsonResponse
def root_redirect(request):
    return redirect('/api/')

# Placeholder API views
from .models import Activity, Team, User, Workout, Leaderboard

def activities_view(request):
    activities = Activity.objects.all()
    data = [
        {
            "id": a.id,
            "user": a.user.name if a.user else None,
            "type": a.type,
            "duration": a.duration
        } for a in activities
    ]
    return JsonResponse(data, safe=False)

def teams_view(request):
    teams = Team.objects.all()
    data = [
        {
            "id": t.id,
            "name": t.name
        } for t in teams
    ]
    return JsonResponse(data, safe=False)

def users_view(request):
    users = User.objects.all()
    data = [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "team": u.team.name if u.team else None
        } for u in users
    ]
    return JsonResponse(data, safe=False)

def workouts_view(request):
    workouts = Workout.objects.all()
    data = [
        {
            "id": w.id,
            "name": w.name,
            "description": w.description,
            "team": w.team.name if w.team else None
        } for w in workouts
    ]
    return JsonResponse(data, safe=False)

def leaderboard_view(request):
    leaderboard = Leaderboard.objects.all()
    data = [
        {
            "id": l.id,
            "user": l.user.name if l.user else None,
            "points": l.points
        } for l in leaderboard
    ]
    return JsonResponse(data, safe=False)
"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({
        "activities": f"{base_url}activities/",
        "teams": f"{base_url}teams/",
        "users": f"{base_url}users/",
        "workouts": f"{base_url}workouts/",
        "leaderboard": f"{base_url}leaderboard/"
    })

urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/activities/', activities_view),
    path('api/teams/', teams_view),
    path('api/users/', users_view),
    path('api/workouts/', workouts_view),
    path('api/leaderboard/', leaderboard_view),
]
