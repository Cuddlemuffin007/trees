from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=20)
    scientific_name = models.CharField(max_length=40)
    wood = models.CharField(max_length=10, choices=[('hard', 'Hardwood'), ('soft', 'Softwood')])
    type_tree = models.CharField(max_length=10, choices=[('dec', 'Deciduous'), ('con', 'Coniferous')])
    max_height = models.IntegerField()
    location = models.CharField(max_length=15)
    uses = models.CharField(max_length=50)

    def __str__(self):
        return self.name
