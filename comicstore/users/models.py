from django.db import models
from db.baseModels import BaseModels
from usual.Gethash import gethash
# Create your models here.
class Usermanager(models.Manager):
    def add_one_user(self,username,password,email):
        if self.get(username=username):
            adduser=None
        else:
            adduser = self.create(username=username,password=gethash(password),email=email)
        return adduser

    def get_one_user(self,username,password):
        try:
            adduser = self.get(username=username,password=password)
        except Exception as e:
            adduser = None
        return adduser


class userparty(BaseModels):
    username = models.CharField(max_length=20,verbose_name='姓名')
    password = models.CharField(max_length=40,verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱地址')
    is_active = models.BooleanField(default=False,verbose_name='激活状态')

    def __str__(self):
        return self.username

    objects = Usermanager()

    class Meta():
        db_table = 'usertable'





