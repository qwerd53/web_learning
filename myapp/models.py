from django.db import models
from datetime import datetime
# Create your models here.

class Users(models.Model):
    '''自定义Stu表对应的Model类'''
    #定义属性：默认主键自增id字段可不写
    id = models.AutoField("学号",primary_key=True)
    name = models.CharField("姓名",max_length=16)
    age = models.SmallIntegerField("年龄")
    phone = models.CharField("电话",max_length=16)
    addtime=models.DateTimeField(default=datetime.now)

    # 定义默认输出格式

    # 自定义对应的表名，默认表名：myapp_stu
    #class Meta:
    # db_table="stu"