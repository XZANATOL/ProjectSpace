from django.db import models

# Create your models here.
class work_experience(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    company = models.TextField()
    date = models.TextField()
    highlights = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['pk']

class recent_projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.TextField()
    link = models.URLField(max_length=500)

    class Meta:
        verbose_name_plural = "Recent_Projects"
        ordering = ['-pk']

    def __str__(self):
        return '{} - {}'.format(self.pk, self.title)