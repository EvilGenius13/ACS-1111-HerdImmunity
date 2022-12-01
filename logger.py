class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        f = open(self.file_name, "w")
        f.write("# Simulation Base Information:\n")
        f.write(f"+ Population: {pop_size}\n")
        f.write(f"+ Percent Population Vaccinated: {vacc_percentage}\n")
        f.write(f"+ Virus Name: {virus_name}\n")
        f.write(f"+ Virus Mortality Rate: {mortality_rate}\n")
        f.write(f"+ Virus Reproduction Rate: {basic_repro_num}\n")
        f.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        pass

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_counter, population_alive, population_infected, population_dead, newly_infected, newly_dead):
        f = open(self.file_name, "a")
        f.write(f"## Iteration : {time_step_counter}\n")
        f.write(f"+ Population Alive : {population_alive}\n")
        f.write(f"+ Population Infected : {population_infected}\n")
        f.write(f"+ Population Dead : {population_dead}\n")
        f.write(f"+ Newly Infected : {newly_infected}\n")
        f.write(f"+ Newly Dead : {newly_dead}\n")
        f.close()

    # ! Logging Functions for testing purposes
    def log_create_population(self, vaccinated, unvaccinated, infected):
        f = open(self.file_name, "a")
        f.write(f"```diff\n")
        f.write(f"! create_population() !\n")
        f.write(f"+ Vaccinated : {vaccinated}\n")
        f.write(f"+ Unvaccinated : {unvaccinated}\n")
        f.write(f"+ Infected : {infected}\n")
        f.write(f"```\n")
        f.close()
    
    def log_simulation_should_continue(self, check_dead, check_vac, check_alive):
        f = open(self.file_name, "a")
        f.write(f"```diff\n")
        f.write(f"! simulation_should_continue() !\n")
        f.write(f"+ Alive : {check_alive}\n")
        f.write(f"+ Dead : {check_dead}\n")
        f.write(f"+ Vaccinated : {check_vac}\n")
        f.write(f"```\n")
        f.close()

    def log_run(self):
        pass

    def log_person_randomizer(self, random_person_id, random_person_vac, random_person_virus):
        f = open(self.file_name, "a")
        f.write(f"```diff\n")
        f.write(f"! Person Randomizer !\n")
        f.write(f"+ ID : {random_person_id}\n")
        f.write(f"+ Vaccinated? : {random_person_vac}\n")
        f.write(f"+ Infected? : {random_person_virus}\n")
        f.write(f"```\n")
        f.close()

