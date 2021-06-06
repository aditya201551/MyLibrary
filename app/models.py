from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    feedback=models.TextField()

    def __str__(self):
        return str(self.user.username)

class Book(models.Model):
    name = models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    course_itr=(
        ('null','Select Branch'),
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MCA','MCA'),
        ('ME', 'B.Tech. ME'),
        ('CSE', 'B.Tech. CSE'),
        ('EI', 'B.Tech. EI'),
        ('EC', 'B.Tech. EC'),
        ('IT', 'B.Tech. IT'),
        ('CE', 'B.Tech. CIVIL'),
        ('EE', 'B.Tech. ELECTRICAL ENGG')
    )
    course=models.CharField(max_length=255, choices=course_itr, default='null')

    semester_itr=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    )

    semester=models.CharField(max_length=5,choices=semester_itr, default='1')

    subject = models.CharField(max_length=255)
    book=models.FileField(upload_to='books/')

    def __str__(self):
        return self.name+" | "+self.course

    def delete(self):
        self.book.storage.delete(str(self.book))
        super(Book, self).delete()
