class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self,name,pet_type,owner=''):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self.pet_type = pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type

class Owner:

    def __init__(self,name):
        self.name = name
    
    def pets(self):
        return Pet.all
    
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception('Could not add pet')

    def get_sorted_pets(self):
        sort_pets = sorted(Pet.all, key=lambda x: x.name)
        return sort_pets

# jim = Pet("Jim Jr.", "panda")
# print(jim.pet_type)

