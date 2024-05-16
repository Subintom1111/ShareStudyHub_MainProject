from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models import Q



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        TEACHER="TEACHER",'Teacher'
        STUDENT="STUDENT",'Student'


    role = models.CharField(max_length=50,choices=Role.choices)
    course = models.CharField(max_length=100, blank=True, null=True)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12, unique=True)
    course = models.CharField(max_length=100, blank=True, null=True)
      # You can adjust the max_length as needed
    



class Profilete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12, unique=True)  # You can adjust the max_length as needed
   

    def _str_(self):
        return self.user.username
    




from django.db import models

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    assigned_teachers = models.CharField(max_length=255)
    credit_hours = models.PositiveIntegerField()
    course_fee = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name






from django.db import models

class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



from django.db import models

class ExamMark(models.Model):
    course_name = models.CharField(max_length=100)
    question_number = models.IntegerField()
    total_marks = models.IntegerField()
    exam_time = models.CharField(max_length=20)  # Add the exam_time field


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the student who made the submission
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)  # Link to the assignment
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the submission was made
    document = models.FileField(upload_to='submissions/')  # Upload a file as the submission


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    

class CourseNotes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='course_notes/')
    
    

    def __str__(self):
        return self.title
    
    

# models.py

from django.db import models

class prepare_exam(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration_in_minutes = models.PositiveIntegerField()
    date = models.DateField()
    start_time = models.TimeField()
    number_of_questions = models.PositiveIntegerField()
    # pass_mark = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    


    # models.py

from django.db import models

class Product(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/product_images/') # Define ImageField
    isbn = models.CharField(max_length=13, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    


class DeliveryAddress(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address_type = models.CharField(max_length=20, choices=(('Home', 'Home'), ('Work', 'Work')))



class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs
    
class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)