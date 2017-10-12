from edc_pharma.constants import MILLIGRAM, CAPSULE, VIAL


class MedicationDefinition:
    def __init__(self, name=None, description=None, category=None,
                 unit=None, milligram=None, total=None,
                 number_of_times_per_day=None,):
        self.name = name
        self.description = description
        self.category = category
        self.unit = unit
        self.milligram = milligram
        self.total = total
        self.number_of_times_per_day = number_of_times_per_day


medications = {}
ambisome = MedicationDefinition(
    name='ambisome',
    description='Ambisome 10 mg/kg/day',
    category=VIAL,
    unit=MILLIGRAM,
    milligram=10,
    total=500,
    number_of_times_per_day=4)
medications.update({'ambisome': ambisome})

fluconazole = MedicationDefinition(
    name='fluconazole',
    description='Fluconazole 800mg/day',
    category=VIAL,
    unit=MILLIGRAM,
    milligram=1200,
    total=500,
    number_of_times_per_day=4)
medications.update({'fluconazole': fluconazole})

flucytosine = MedicationDefinition(
    name='flucytosine',
    description='Flucytosine 100mg/kg/day',
    category=CAPSULE,
    unit=MILLIGRAM,
    milligram=100,
    total=500,
    number_of_times_per_day=4,)
medications.update({'flucytosine': flucytosine})

amphotericin = MedicationDefinition(
    name='amphotericin',
    description='Amphotericin B 1 mg/kg',
    category=CAPSULE,
    unit=MILLIGRAM,
    milligram=1,
    total=50,
    number_of_times_per_day=4)
medications.update({'amphotericin': amphotericin})
