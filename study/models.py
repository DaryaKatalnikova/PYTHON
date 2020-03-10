from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Test(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Quest(models.Model):
    question = models.CharField(max_length=200)
    tip=models.CharField(max_length=1)
    test = models.ForeignKey('Test',on_delete=models.CASCADE,)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=200)
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE,)

    def __str__(self):
        return self.answer

class School(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#class UserManager(BaseUserManager):
 #   def create_user(self, email, password=None):
  #      """
   #     Creates and saves a User with the given email and password.
    #    """
#
 #       user = self.model(
  #          email=self.normalize_email(email),
   #     )
#
 #       user.set_password(password)
  #      user.save(using=self._db)
   #     return user


    #def create_staffuser(self, email):
     #   """
      #  Creates and saves a staff user with the given email and password.
       # """
        #user = self.create_user(
        #    email,
         #   password=password,
        #)
        #user.staff = True
        #user.save(using=self._db)
        #return user



class User(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #active = models.BooleanField(default=True)
    #staff = models.BooleanField(default=False)
    #admin = models.BooleanField(default=False)


    #def get_full_name(self):
     #   return self.email

   # def get_short_name(self):
    #    return self.email

   # def __str__(self):
      #  return self.email

   # def has_perm(self, perm, obj=None):
    #    "Does the user have a specific permission?"
     #   return True

    #def has_module_perms(self, app_label):
     #   "Does the user have permissions to view the app `app_label`?"
      #  return True

   # @property
    #def is_staff(self):
     #   return self.staff

    #@property
    #def is_admin(self):
     #   "Is the user a admin member?"
      #  return self.admin

    #@property
    #def is_active(self):
     #   return self.active
      #  "Is the user active?"


class Useranswer(models.Model):
    answer = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
