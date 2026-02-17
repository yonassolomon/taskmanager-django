from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES=[
        ('high','🔴 High'),
        ('medium','🟡 Medium'),
        ('low','🟢 Low'),
    ]
    user=models.ForeignKey(User,on_delete=CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True,blanck=True ) #blank=True = Forms can be submitted with this field empty
    completed=models.BooleanField(default=False)
    priority=models.CharField(max_length=10,choices=PRIORITY_CHOICES,default='medium')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created_date']
