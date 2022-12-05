import random, sys, argparse
from person import Person
from logger import Logger
from virus import Virus
from progress.spinner import PixelSpinner


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
        self.total_alive = self.pop_size
        self.total_dead = 0
        self.total_infected = 0
        self.change_infected = initial_infected
        self.total_vaccinated = 0
        self.change_vaccinated = 0
        self.change_dead = 0
        
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
            self.change_vaccinated += 1 
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

        vac_per = self.vacc_percentage * 100
        vir_mor_per = self.virus.mortality_rate * 100
        vir_rep_per = self.virus.repro_rate * 100

        self.logger.start_interaction_log()
        self.logger.write_metadata(self.pop_size, vac_per, virus.name, vir_mor_per, vir_rep_per, self.initial_infected)
        self.logger.log_create_population(vaccinated_group, unvaccinated_group, infected_group, self.pop_size)
        return start_population

    # ? TESTING FUNCTION
    def _sim_change_percent(self, num1, num2):
        if num1 == 0:
            return -100
        elif num2 == 0:
            return "Inf"
        else:
            return round(((num1 - num2) / num2 ) * 100, 2)
    
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

        # ! STAGING AREA
        change_alive = self._sim_change_percent(sim_check_alive, self.total_alive)
        change_infected = self._sim_change_percent(sim_check_infections, self.change_infected)
        change_vaccinated = self._sim_change_percent(sim_check_vaccinated, self.change_vaccinated)
        change_dead = self._sim_change_percent(sim_check_dead, self.change_dead)
        self.total_alive = sim_check_alive
        self.change_infected = sim_check_infections
        self.change_vaccinated = sim_check_vaccinated
        self.change_dead = sim_check_dead

        self.logger.log_simulation_should_continue(self.time_step_counter, sim_check_dead, change_dead, sim_check_vaccinated, 
            change_vaccinated, sim_check_alive, change_alive, sim_check_infections, change_infected)
        
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

    # * OKAY
    def run(self):
        print(f"Simulation started. Please click on the log to view updates.")
        self.time_step_counter = 0
        should_continue = True


        while should_continue:
            calc = "Calculating Iteration " + str(self.time_step_counter) + " "
            #print(f"Calculating Iteration {self.time_step_counter}")
            bar = PixelSpinner(calc, max=1)
            for i in range(1):
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            
                self.time_step_counter += 1
                self.time_step()
                self._infect_newly_infected()
            #self.total_alive = self.pop_size - self.total_dead
            #self.logger.log_time_step(self.time_step_counter, self.total_alive, self.total_infected, self.total_dead,)
                should_continue = self._simulation_should_continue()
                bar.next()
            bar.finish()
        print(f"Simulation complete after {self.time_step_counter} iterations.")
        #TODO: LOGGER FOR FINAL STATUS 


        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    # * OKAY
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


    # * OKAY    
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

    # * OKAY
    def _infect_newly_infected(self):
        #newly_infected_num = len(self.newly_infected)
        #self.logger.log_newly_infected(newly_infected_num)
        for infected_person in self.newly_infected:
            infected_person.infection = self.virus
            self.total_infected += 1
        self.newly_infected = []
        
        
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
    


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Hydra"
    repro_num = 0.2
    mortality_rate = 0.4
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 50000
    vacc_percentage = 0.1
    initial_infected = 100

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()