from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from . import models as db
import re


def post_description_extractor(text):
	"""Parses HTML text and returns plain text using regex"""
	pattern = r">(.[^<>]+)<"
	results = re.findall(pattern, text)
	string = ""
	for result in results:
		string += " " + result
	return string[:300]


def post_list_parser(order=None, cat=None):
	"""Queries a group of posts and returns a list of parsed posts along
	along with their header image"""
	if order:
		objects = db.post.objects.filter(status="Published").order_by(f"-{order}")[:3]
	else:
		objects = db.post.objects.filter(status="Published", cat=cat)

	posts_list = [] # List of parsed posts
	for post in objects:
		try:
			img = db.images.objects.filter(post=post.title, title="header")[0]
		except:
			# Create an empty object with 'image' attribute of None
			img = type('img', (object,), {"image":None})()
		posts_list.append({
			"title": post.title,
			"cat": post.cat,
			"slug": post.slug,
			"created": post.created,
			"updated": post.updated,
			"body": post_description_extractor(post.body[:500]),
			"img": img.image,
			})
	# Return results
	return posts_list


def blog_home(request):
	"""Returns the blog home page with context of
	the newest add & updated posts, and the available categories"""
	latest_posts = post_list_parser(order="created")
	updated_posts = post_list_parser(order="updated")
	categories = db.category.objects.all()
	# Add context for render
	context = {
		"latest": latest_posts,
		"updated": updated_posts,
		"categories": categories,
	}
	return render(request, "blog_home.html", context)


def posts_in_cat(request, cat):
	"""Returns posts inside a category"""
	cat_validator = get_object_or_404(db.category, title=cat)
	posts = post_list_parser(cat=cat)
	# Add context for render
	context = {
		"cat": cat,
		"posts": posts,
		"count": len(posts),
	}
	return render(request, "posts_in_cat.html", context)


def post_in_detail(request, cat, slug):
	"""Returns a detailed full post"""
	post = get_object_or_404(db.post, cat=cat, slug=slug)
	images = db.images.objects.filter(post=post.title)
	# Add context for render
	context = {
		"title": post.title,
		"cat": post.cat,
		"slug": post.slug,
		"body": post.body,
		"created": post.created,
		"updated": post.updated,
		"images": images
	}
	for img in images:
		context[img.title] = img.image
	return render(request, "post_in_detail.html", context)


@require_http_methods(["POST"])
def send_msg(request):
    message = f"""
    Django Blog Feedback Form:

    Name: {request.POST["name"]}
    Email: {request.POST["email"]}
    Subject: {request.POST["subject"]}
    Message: {request.POST["message"]}

    """
    # send_mail(subject, message, sender_email, [recivers])
    send_mail(
        "Django Blog Feedback Form",
        message,
        "",
        ["abdelrahmanbedox@gmail.com"],
        fail_silently=False
        )
    return redirect(f"/blog/{str(request.POST['url'])}")