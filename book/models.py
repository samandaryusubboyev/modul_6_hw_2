from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    author = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

