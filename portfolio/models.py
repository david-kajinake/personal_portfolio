from django.db import models
from django.utils import timezone
import time

def get_time():
    localtime = time.localtime()
    return f"{localtime.tm_year}{localtime.tm_mon}{localtime.tm_yday}{localtime.tm_mday}{localtime.tm_wday}{localtime.tm_hour}{localtime.tm_min}{localtime.tm_sec}"

#Create your models here.z
class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    github_repo_link = models.CharField(max_length = 1000)
    live_demo_link = models.CharField(max_length = 1000)
    image = models.ImageField(blank= True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length= 250)
    description = models.TextField(max_length=100000)
    image = models.ImageField(blank= True)
    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length = 100 , blank = False)
    project_used_on = models.ManyToManyField(Project , related_name="technologies")
    def __str__(self):
        return self.name

"""class Image(models.Model):
    photo = models.ImageField(blank= True)
    project = models.ForeignKey(Project , on_delete= models.DO_NOTHING , related_name= "images" , blank= True )
    technology = models.ForeignKey(Technology , on_delete= models.DO_NOTHING , related_name= "images"  , blank = True)
   # service = models.ForeignKey(Service , on_delete= models.DO_NOTHING , related_name= "images" , blank= True)
    def __str__(self):
        return f"image for {self.project.name}"""

class Contacter(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 100)
    contacter_id  = models.CharField(max_length= 250  , blank= True)
    contacted_at = models.DateField( auto_now_add= True , blank = True )
    def save(self , *args , **kwargs , ):
        if not self.pk: 
            current_time = get_time()
            self.contacter_id = f"{current_time}" 
        super().save(*args , **kwargs)
    def __str__(self):
        return self.name


class Message(models.Model):
    contacter = models.ForeignKey(Contacter , on_delete= models.CASCADE , related_name="messages")
    content = models.TextField(max_length= 10000)
    created_at = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.contacter.name
    
class Faq(models.Model):
    question = models.CharField(max_length= 100000)
    answer = models.TextField(max_length= 100000)
    def __str__(self):
        return self.question    
    
class MyPhoneNumber(models.Model):
    phone_number = models.CharField(max_length= 255)
    def __str__(self):
        return self.phone_number

class MyEmail(models.Model):
    email_address = models.EmailField(max_length= 255)
    def __str__(self):
        return self.email_address






