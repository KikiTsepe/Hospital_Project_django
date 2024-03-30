from django_filters import FilterSet


class HumanFilter(FilterSet):

    class Meta:
        fields = {
            'name': ['exact', 'contains', 'icontains'],
            'age': ['exact', 'gte', 'lte'],
        }


class EmployeeFilter(HumanFilter):

    class Meta:
        fields = {
            **HumanFilter.Meta.fields,
            'experience': ['exact', 'gte', 'lte'],
            'salary': ['exact', 'gte', 'lte'],
        }
