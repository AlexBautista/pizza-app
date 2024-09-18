from django.db import models

# Create your models here.
class Order(models.Model):
    customername = models.CharField(max_length=50)
    sinstructions = models.CharField(max_length=100)
  
    FLAVOR1= "Pepperoni"
    FLAVOR2 = "Supreme"
    FLAVOR3 = "Chicago"

    PIZZA_CHOICES = {
        FLAVOR1: "Pepperoni",
        FLAVOR2: "Supreme",
        FLAVOR3: "Chicago",
    }
    
    pizza_flavor = models.CharField(
        max_length=20,
        choices=PIZZA_CHOICES,
        default=FLAVOR1,
    )

    def __str__(self):
        return self.customername + ' ' + self.pizza_flavor
      
    #def is_upperclass(self):
    #    return self.pizza_flavor in {self.FLAVOR3, self.FLAVOR1}