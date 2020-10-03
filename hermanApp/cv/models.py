from django.db import models

class cv(models.Model):
    image = models.FilePathField( path="/images",max_length=100) 
    langage = models.CharField(max_length=100)
    title = models.CharField( max_length=100)
    decription = models.TextField()

    def __str__(self):
        return self.title
    
