from django.db.models import Q
from goods.models import Products
from django.db.models.functions import Lower


def query_search(query):
    words = [i for i in query.split() if len(i) > 2]
    q_objects = Q()

    for item in words:
        q_objects |= Q(description__icontains = item)
        q_objects |= Q(name__icontains = item)

    return Products.objects.filter(q_objects)