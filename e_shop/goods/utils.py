from django.db.models import Q
from goods.models import Products

def query_search(query):
    words = [i for i in query.strip().split() if len(i) > 3]
    q_objects = Q()

    for item in words:
        q_objects |= Q(description__icontains = item)
        q_objects |= Q(name__icontains = item)
    
    return Products.objects.filter(q_objects)