from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    # You can add more fields as needed

    def __str__(self):
        return self.title

class Section(models.Model):
    article = models.ForeignKey(Article, related_name='sections', on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}: {self.header}"
