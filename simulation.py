import random, sys
from person import Person
from logger import Logger
from virus import Virus

# * OKAY
class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.virus = virus
        self.pop_size = pop_size 
        self.vacc_percentage = vacc_percentage 
        self.initial_infected = initial_infected 
        
        self.newly_infected = []
        self.body_bag = []
        self.total_alive = 0
        self.total_dead = 0
        self.total_infected = 0
        self.total_vaccinated = 0
        
        self.time_step_counter = 0
        self.file_name = f"{virus.name}.{pop_size}.{vacc_percentage}.{initial_infected}.md"
        self.logger = Logger(self.file_name)
        self.population = self._create_population()

    # * OKAY
    def _create_population(self):
        start_population = []
        #Vaccinated
        vaccinated_group = self.pop_size * self.vacc_percentage
        vaccinated_group = int(vaccinated_group)
        self.current_vaccinated = vaccinated_group
        #Unvaccinated
        unvaccinated_group = self.pop_size - self.initial_infected - vaccinated_group
        #Infected
        infected_group = self.initial_infected

        id_num = 0
        for num in range(vaccinated_group):
            id_num += 1 
            person = Person(id_num, True, None)
            start_population.append(person)
        
        for num in range(unvaccinated_group):
            id_num += 1
            person = Person(id_num, False, None)
            start_population.append(person)
        
        for num in range(infected_group):
            id_num += 1
            self.total_infected += 1
            person = Person(id_num, False, self.virus)
            start_population.append(person)

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)
        self.logger.log_create_population(vaccinated_group, unvaccinated_group, infected_group)
        return start_population

    # * OKAY
    def _simulation_should_continue(self):
        sim_check_dead = 0
        sim_check_vaccinated = 0
        sim_check_alive = 0
        sim_check_infections = 0
        
        for person in self.body_bag:
            if person.is_alive == False:
                sim_check_dead += 1
        for person in self.population:
            if person.is_vaccinated == True:
                sim_check_vaccinated += 1
        for person in self.population:
                sim_check_alive += 1
        for person in self.population:
            if person.infection:
                sim_check_infections += 1

        self.logger.log_simulation_should_continue(sim_check_dead, sim_check_vaccinated, sim_check_alive, sim_check_infections)
        
        if sim_check_dead == self.pop_size:
            return False
        elif sim_check_infections == 0:
            return False
        else: 
            return True
        
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        pass

    # ? PRODUCTION ATTEMPT
    def run(self):
        print(f"Simulation started. Please click on the log to view updates")
        self.time_step_counter = 0
        should_continue = True


        while should_continue:
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            
            self.time_step_counter += 1
            self.time_step()
            self._infect_newly_infected()
            should_continue = self._simulation_should_continue()
        print(f"Simulation complete after {self.time_step_counter} steps.")
        #TODO: LOGGER FOR FINAL STATUS 


        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    # ? PRODUCTION ATTEMPT
    def time_step(self):
        interaction_length = 100
        if (len(self.population)) < 100:
            interaction_length = len(self.population)
        
        for person in self.population:
            if person.infection:
                random_sample_group = random.sample(self.population, interaction_length)
                for random_person in random_sample_group:
                    self.interaction(person, random_person)
                chance_of_death = random.random()
                if chance_of_death < virus.mortality_rate:
                    person.is_alive = False
                    person.infection = False
                    self.body_bag.append(person)
                    self.total_dead += 1
                    self.population.remove(person)
                    self.total_infected -= 1
                else:
                    person.is_vaccinated = True
                    person.infection = None
                    self.total_vaccinated += 1
                    self.total_infected -= 1
                        
        
        
        self.total_alive = self.pop_size - self.total_dead
        self.logger.log_time_step(self.time_step_counter, self.total_alive, self.total_infected, self.total_dead,)                  
        
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        pass


    # ? PRODUCTION ATTEMPT    
    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        
        if random_person.is_vaccinated == False and random_person.infection == None:
            chance_of_infection = random.random()
            if chance_of_infection < virus.repro_rate:
                self.newly_infected.append(random_person)

        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.

    # ? PRODUCTION ATTEMPT
    def _infect_newly_infected(self):
        newly_infected_num = len(self.newly_infected)
        self.logger.log_newly_infected(newly_infected_num)
        for infected_person in self.newly_infected:
            infected_person.infection = self.virus
            self.total_infected += 1
        self.newly_infected = []
        
        
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
    


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 10000
    vacc_percentage = 0.2
    initial_infected = 50

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()