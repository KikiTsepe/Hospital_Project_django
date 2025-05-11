from django_filters import FilterSet, NumberFilter
from entities.models import Room


class RoomFilter(FilterSet):
    free_beds__gte = NumberFilter(field_name="free_beds",
                                  lookup_expr="gte",
                                  required=False)
    free_beds__lte = NumberFilter(field_name="free_beds",
                                  lookup_expr="lte",
                                  required=False)
    num_nurses__gte = NumberFilter(field_name="num_nurses",
                                   lookup_expr="gte",
                                   required=False)
    num_nurses__lte = NumberFilter(field_name="num_nurses",
                                   lookup_expr="lte",
                                   required=False)
    num_patients__gte = NumberFilter(field_name="num_patients",
                                     lookup_expr="gte",
                                     required=False)
    num_patients__lte = NumberFilter(field_name="num_patients",
                                     lookup_expr="lte",
                                     required=False)

    class Meta:
        model = Room
        fields = {"number": ["exact"], "capacity": ["exact", "gte", "lte"]}
