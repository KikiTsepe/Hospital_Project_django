from entities.filters.base_filters import EmployeeFilter
from entities.models import Nurse


class NurseFilter(EmployeeFilter):

    class Meta:
        model = Nurse
        fields = {**EmployeeFilter.Meta.fields, "room_in_carge": ["exact"]}
