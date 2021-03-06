from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=256)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def getId(self):
        return self.id

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password


class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=400)
    users = models.ManyToManyField(User)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=22)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_visible = models.BooleanField(max_length=1)
    joined_users = models.TextField()


class Relationship(models.Model):
    id = models.AutoField(primary_key=True)
    user_one_id = models.IntegerField(default=0)
    user_two_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    action_user_id = models.IntegerField(default=0)
