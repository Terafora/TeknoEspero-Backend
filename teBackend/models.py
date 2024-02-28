from django.db import models

# Blog Model

class Blog(models.Model):
    """A blog item which contains the content for posts"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
