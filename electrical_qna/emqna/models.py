from django.db import models
from django.contrib.auth.models import User

class QnaRecord(models.Model):
    # Field Count: 5
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    question_text = models.TextField() 
    answer_text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question_text[:30]}"