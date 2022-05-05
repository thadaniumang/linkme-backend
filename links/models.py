from django.db import models
from users.models import Profile


class LinkList(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.title
    

class Links(models.Model):
    link_list = models.ForeignKey(LinkList, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
