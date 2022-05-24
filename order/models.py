from django.db import models
from django.contrib.auth import get_user_model
from product.models import NewProduct

User = get_user_model()
STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_process', 'В обработке'),
    ('closed', 'Закрыт'),
)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.RESTRICT)
    product = models.ForeignKey(NewProduct, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')
    product = models.ManyToManyField(NewProduct, through=OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
