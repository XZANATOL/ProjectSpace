from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.core.mail import send_mail


from . import models as db
from blog.views import post_list_parser

def portfolio(request):
    """ Loads the portoflio website """
    # Data to load: work-experience / projects / blog recent posts 
    work_exp = db.work_experience.objects.order_by('pk')
    projects = db.recent_projects.objects.order_by('-pk')
    latest_posts = post_list_parser(order="created")
    work_exp_parsed = []
    projects_parsed = []
    for role in work_exp:
        work_exp_parsed.append({
                "title": role.title,
                "company": role.company,
                "date": role.date,
                "highlights": role.highlights.replace("\r", "").split("\n")
                })
    for project in projects:
        projects_parsed.append({
                "title": project.title,
                "description": project.description,
                "image": project.image,
                "link": project.link
            })
    # Rendering Output
    context = {
            "work_exp":work_exp_parsed,
            "projects":projects_parsed,
            "latest": latest_posts
            }
    return render(request, 'home.html', context, status=200)


@require_http_methods(["POST"])
def send_msg(request):
    message = f"""
    Django Portfolio Contact Form:

    Name: {request.POST["name"]}
    Email: {request.POST["email"]}
    Subject: {request.POST["subject"]}
    Message: {request.POST["message"]}

    """
    # send_mail(subject, message, sender_email, [recivers])
    send_mail(
        "Django Contact Form",
        message,
        "",
        ["abdelrahmanbedox@gmail.com"],
        fail_silently=False
        )
    return redirect("/portofolio/#Contact")


def page_404(request, exception=None):
    """ Handler for 404 requests """
    return render(request, "404.html", status=404)