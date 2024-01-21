from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class DemoNote(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.body}" + self.hyperlinked_title()
    
    def hyperlinked_title(self):
        
        # return link with a reverse_lazy
        return "A"
        #return f"<a href='{reverse_lazy('notesdemo:detail', kwargs={'pk': self.pk})}'>{self.title}</a>"