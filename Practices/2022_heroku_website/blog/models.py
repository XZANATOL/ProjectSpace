from django.db import models

# Create your models here.
class category(models.Model):
	title = models.CharField(max_length=250, primary_key=True)

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.title


class post(models.Model):
	STATUS_CHOICES = (
		("Draft", "draft"),
		("Published", "published")
		)
	cat = models.ForeignKey(category, on_delete=models.CASCADE)

	title = models.CharField(max_length=250, primary_key=True)
	slug = models.CharField(max_length=250)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices= STATUS_CHOICES, default="Draft") 

	class Meta:
		ordering = ["-status"]

	def __str__(self):
		return self.title



class images(models.Model):
	post = models.ForeignKey(post, on_delete=models.CASCADE)
	title = models.CharField(max_length=250, default="")
	image = models.TextField()

	class Meta:
		verbose_name_plural = "images"

	def __str__(self):
		return self.title