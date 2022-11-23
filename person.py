import random
from virus import Virus


class Person(object):
   
    def __init__(self, _id, is_vaccinated, infection = None):
        
        self._id = _id  # probably should tick up by number
        self.is_alive = True #should start true
        self.is_vaccinated = is_vaccinated #have to set to none?
        self.infection = infection #seems to be none

    def did_survive_infection(self):
        # TODO Only called if infection attribute is not None.
        chance_of_infection = random.random()
        # Check generate a random number between 0.0 - 1.0
        # If the number is less than the mortality rate of the 
        # person's infection they have passed away. 
        # Otherwise they have survived infection and they are now vaccinated. 
        # Set their properties to show this
        # TODO: The method Should return a Boolean showing if they survived.
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
    
def infection_survival_test():
    virus = Virus("CoinFlip", 0.7, 0.5)
    test_infection_person = Person(4, False, virus)
    assert test_infection_person._id == 4
    assert test_infection_person.is_alive is True
    assert test_infection_person.is_vaccinated is False
    assert test_infection_person.infection is virus
    #TODO: Need to test how if they survive in a test
    surival_chance = test_infection_person.did_survive_infection()
    if surival_chance:
        assert test_infection_person.is_alive is True
        assert test_infection_person.is_vaccinated is True
        assert test_infection_person.infection is None

    else:
        assert test_infection_person.is_alive is False
        assert test_infection_person.is_vaccinated is False




if __name__ == "__main__":
    print('***Friendly reminder that assertions only pop if they fail***')
    vaccinated_person_test()
    unvaccinated_person_test()
    infected_person_test()
    infection_survival_test()

    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 
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
    print(f"Mortality Rate: {death_count / 100 }")

    # TODO Loop over all of the people 
    # TODO If a person is_alive True add one to did_survive
    # TODO If a person is_alive False add one to did_not_survive

    # TODO When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.