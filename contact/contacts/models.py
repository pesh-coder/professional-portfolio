from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
