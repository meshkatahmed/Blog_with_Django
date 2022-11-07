from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title = models.CharField(max_length=264,verbose_name="put a title")
    slug = models.SlugField(max_length=264,unique=True)
    blog_content = models.TextField(verbose_name="what's on your mind")
    blog_image = models.ImageField(upload_to="static/media/images/blogimages",blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment = models.TextField(verbose_name="Write your comment")
    comment_date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-comment_date',]
    def __str__(self):
        return self.comment

class Like(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_like')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker_user')

    def __str__(self):
        return self.user + 'likes' + self.blog
