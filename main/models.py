from django.db import models



class Post(models.Model):

    name = models.CharField(verbose_name = "Должность", max_length = 150)


    def __str__(self) -> str:

        return self.name
    
    class Meta:

        verbose_name = "Должность"
        verbose_name_plural = "Должность"

class Worker(models.Model):

    firstName = models.CharField(verbose_name = "Фамилия", max_length = 155)
    lastName = models.CharField(verbose_name = "Имя", max_length = 155)
    age = models.PositiveIntegerField(verbose_name = "Возраст")
    post = models.ForeignKey(Post, verbose_name = "Должность", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        
        return self.firstName + " " + self.lastName
    

    class Meta:
        
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"






