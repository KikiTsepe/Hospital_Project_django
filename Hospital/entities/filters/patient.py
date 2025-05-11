from entities.filters.base_filters import HumanFilter
from entities.models import Patient


class PatientFilter(HumanFilter):

    class Meta:
        model = Patient
        fields = {
            **HumanFilter.Meta.fields, "disease":
            ["exact", "contains", "icontains"],
            "room__number": ["exact"],
            "doctor": ["exact"]
        }
