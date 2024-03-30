from django_filters import NumberFilter
from entities.filters.base_filters import EmployeeFilter
from entities.models import Doctor


class DoctorFilter(EmployeeFilter):
    patient__gte = NumberFilter(field_name="num_patients",
                                lookup_expr="gte",
                                required=False)
    patient__lte = NumberFilter(field_name="num_patients",
                                lookup_expr="lte",
                                required=False)

    class Meta:
        model = Doctor
        fields = EmployeeFilter.Meta.fields
