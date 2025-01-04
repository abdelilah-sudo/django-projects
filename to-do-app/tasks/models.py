from django.db import models
from django.contrib.auth.models import User  # Import User model
from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length=50)  # Increased max_length for more flexibility
    description = models.TextField(null=True,blank=True)
    deadline = models.DateField(default=datetime.now())  # Corrected default callable for datetime.now
    status = models.BooleanField(default=False)  # Default is False for pending
    added = models.DateTimeField(auto_now_add=True)  # Timestamp when the task is created
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed to ForeignKey, not OneToOneField

    class Meta:
        ordering = ['deadline']  # Default ordering by deadline

    def __str__(self):
        return f"{self.title} - {'Completed' if self.status else 'Pending'}"
