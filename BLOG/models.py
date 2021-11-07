from django.db import models


from users_app.models import NewUser
# Create your models here.



class Blog_Post(models.Model):
    AuthorName =models.ForeignKey(NewUser, on_delete=models.CASCADE )
    Title = models.CharField(max_length =250)
    Body = models.TextField(max_length =250)
    blog_img = models.ImageField(upload_to="blogImage", blank=True,  null=True,)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"  {self.AuthorName} =>> {self.Title}"