from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(models.Model):
    p_name = models.CharField(max_length=100)

    def __str__(self):
        return self.p_name
    
class Category(models.Model):
    c_name = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name

class Task(models.Model):
    title = models.CharField(max_length=100)
    decription = models.CharField(max_length = 500)
    deadline = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[("Pending","Pending"),
                 ("In Progress", "In Progress"),
                 ("Completed","Completed"),
                 ],
                 default="pending"
                 )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()
    priority_name = models.CharField(max_length=100)

    def __str__(self):
        return self.task

class SubTask(models.Model):
    parent_task = models.ForeignKey(Task,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title}"