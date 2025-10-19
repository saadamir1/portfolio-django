from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Experience, Project, ContactMessage

def home(request):
    return render(request, 'portfolio/home.html', {
        'name': 'Saad Amir',
        'title': 'Full-Stack Developer'
    })

def about(request):
    return render(request, 'portfolio/about.html', {
        'summary': 'Full-Stack Developer with 1+ year of experience building scalable backend APIs and web applications using NestJS, PostgreSQL, TypeScript, and React.'
    })

def experience(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio/experience.html', {'experiences': experiences})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def skills(request):
    skills = {
        'Languages & Frameworks': ['JavaScript', 'TypeScript', 'Java', 'C++', 'Python', 'Node.js', 'NestJS', 'Express.js'],
        'Frontend': ['React', 'Next.js', 'React Native', 'HTML5', 'CSS3', 'Tailwind CSS'],
        'Backend & Databases': ['PostgreSQL', 'MongoDB', 'TypeORM', 'GraphQL', 'REST APIs', 'JWT'],
        'DevOps': ['Docker', 'Kubernetes', 'AWS', 'Git', 'GitHub Actions', 'CI/CD']
    }
    return render(request, 'portfolio/skills.html', {'skills': skills})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all fields.')
    
    return render(request, 'portfolio/contact.html')