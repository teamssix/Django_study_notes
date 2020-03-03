from django.db import models


# Create your models here.

class BookInfo(models.Model):  # 定义数据信息类模型
	name = models.CharField(max_length=10)  # 设计name属性
	def __str__(self):
		return self.name

class PeopleInfo(models.Model):  # 定义人物信息类模型
	name = models.CharField(max_length=10)
	gender = models.BooleanField()
	book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
	def __str__(self):
		return self.name
