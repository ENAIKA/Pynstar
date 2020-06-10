from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.urls import reverse

# Image model .
#profile model
class UserProfile(models.Model):
    profilephoto = models.ImageField(upload_to = 'profile/')
    bio = models.TextField(max_length=50)    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def update_profile(self,name,field,value):
        obj = UserProfile.objects.get(bio=name)
        obj.field = value
        obj.save()

    def delete_profile(self):
        self.delete()
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()

class Image(models.Model):
    name=models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'photos/')
    caption=models.CharField(max_length =60)
    created_on = models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="liked" )
    posted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
   


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_on']

    def save_image(self):
        self.save()

    def update_caption(self,name,field,value):
        obj = Image.objects.get(caption=name)
        obj.field = value
        obj.save()

    def delete_image(self):
        self.delete()
     
    
    
    @classmethod
    def get_image_by_id(cls,id):
        photos = cls.objects.filter(id=id)
        return photos

    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos

class Comments(models.Model):
    '''
    Comment model
    '''
    comment=models.TextField(max_length=150,default='No comments')
    photo_id=models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    # user=models.ForeignKey(User,related_name='comments', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    '''
    Comment model
    '''
    comment=models.TextField(max_length=150,default='No comments')
    photo_id=models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    

class Follower(models.Model):
    user_from=models.ForeignKey(User, related_name="rel_from_set",on_delete=models.CASCADE)
    user_to=models.ForeignKey(User, related_name="rel_to_set",on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together=('user_from','user_to')

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

User.add_to_class("following",models.ManyToManyField("self",through=Follower, related_name="followers",symmetrical=False))


