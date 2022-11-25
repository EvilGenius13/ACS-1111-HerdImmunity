import random
from virus import Virus

class Person(object):
   
    def __init__(self, _id, is_vaccinated, infection = None):
        
        self._id = _id  
        self.is_alive = True 
        self.is_vaccinated = is_vaccinated 
        self.infection = infection 

    def did_survive_infection(self):
        chance_of_infection = random.random()
        if self.infection:
            if chance_of_infection < self.infection.mortality_rate:
                self.is_alive = False
            else:
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
            return self.is_alive

    # Vaccinated Test
def vaccinated_person_test():
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Unvaccinated Test
def unvaccinated_person_test():
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
   
    # Infected Test
def infected_person_test():
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus
    
    # Infection Survival Test
def infection_survival_test():
    virus = Virus("CoinFlip", 0.7, 0.5)
    test_infection_person = Person(4, False, virus)
    assert test_infection_person._id == 4
    assert test_infection_person.is_alive is True
    assert test_infection_person.is_vaccinated is False
    assert test_infection_person.infection is virus

    surival_chance = test_infection_person.did_survive_infection()
    if surival_chance:
        assert test_infection_person.is_alive is True
        assert test_infection_person.is_vaccinated is True
        assert test_infection_person.infection is None

    else:
        assert test_infection_person.is_alive is False
        assert test_infection_person.is_vaccinated is False

# Testing Area
if __name__ == "__main__":
    print('***Friendly reminder that assertions only pop if they fail***')
    vaccinated_person_test()
    unvaccinated_person_test()
    infected_person_test()
    infection_survival_test()

    # First Full Virus Test
    virus = Virus('Zombie Outbreak', 0.6, 0.3)
    patient_zero = Person('PatientZero', False, virus)
    patient_zero.did_survive_infection()
    people = []
    for i in range(1, 101):
        person = Person(i, False, virus)
        people.append(person)
        person.did_survive_infection()

    death_count = 0
    survived_count = 0
    for person in people:
        if person.is_alive:
            survived_count += 1
        else:
            death_count += 1
    print(f"Surived Count: {survived_count}")
    print(f"Death Count: {death_count}")
    print(f"Comparison: Virus Mortality: {virus.mortality_rate} | Simulation Mortality: {death_count / 100 }")

    # Stretch challenge using Zombie Outbreak Virus
    stretch_infected_people=[]
    for i in range(1, 101):
        person = Person(i, False)
        if random.random() < virus.repro_rate:
            person.infection = virus
            stretch_infected_people.append(person)
    print(f'Infected: {len(stretch_infected_people)}, Uninfected: {100 - len(stretch_infected_people)} ')
