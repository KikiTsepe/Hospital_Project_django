from django_filters import FilterSet
from entities.models import Room


class RoomFilter(FilterSet):

    class Meta:
        model = Room
        fields = {"number": ["exact"], "capacity": ["exact", "gte", "lte"]}
