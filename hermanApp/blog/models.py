from django.db import models

class TimespamtedModel(models.Model):
    created_at  = models.DateField( auto_now_add=True)
    update_at = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
  #  article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Article(TimespamtedModel):
    title= models.CharField( max_length=250)
    content = models.TextField()
    image= models.ImageField(upload_to='blog/images')
    author = models.CharField( max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.title
        
        

class Comment(TimespamtedModel):
    author = models.CharField( max_length=100)
    content = models.TextField()
    article = models.ForeignKey(Article ,on_delete= models.CASCADE)

    def __str__(self):
        return self.author