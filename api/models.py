from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.User", related_name="posts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey(
        "auth.User", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]