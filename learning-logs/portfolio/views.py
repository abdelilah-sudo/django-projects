from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template.exceptions import TemplateDoesNotExist

# Create your views here.
def portfolio_home(request):
    return render(request,'main temps/phome.html')


def about(request):
    return render(request,'main temps/about.html')
def projects(request):
    return render(request,'main temps/projects.html')
def skills(request):
    return render(request,'main temps/skills.html')
def front_projects(request, temp_id, page=""):
    # Handle optional page parameter
    page_suffix = f'_{page}' if page else ""
    template_name = f'front_end temps/template{temp_id}{page_suffix}.html'
    try:
        # Render the appropriate template
        return render(request, template_name)
    except TemplateDoesNotExist:
        # Handle missing templates gracefully
        return HttpResponseNotFound(f"Template not found: {template_name}")
