from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)  # Add this line
    featured_article = models.BooleanField(default=False)
    def __str__(self):
        return self.title
