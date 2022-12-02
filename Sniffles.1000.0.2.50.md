# Simulation Base Information:
+ Population: 1000
+ Percent Population Vaccinated: 0.2
+ Virus Name: Sniffles
+ Virus Mortality Rate: 0.12
+ Virus Reproduction Rate: 0.5
```diff
! create_population() !
+ Vaccinated : 200
+ Unvaccinated : 750
+ Infected : 50
```
## Iteration : 1
+ Population Alive : 994
+ Population Infected : 50
+ Population Dead : 6
```diff
! Infect Newly Infected !
+ Newly Infected : 1724
```
```diff
! simulation_should_continue() !
+ Alive : 994
+ Dead : 6
+ Vaccinated : 239
+ Infected : 686
```
## Iteration : 2
+ Population Alive : 925
+ Population Infected : 1774
+ Population Dead : 75
```diff
! Infect Newly Infected !
+ Newly Infected : 2338
```
```diff
! simulation_should_continue() !
+ Alive : 925
+ Dead : 75
+ Vaccinated : 796
+ Infected : 129
```
## Iteration : 3
+ Population Alive : 909
+ Population Infected : 4112
+ Population Dead : 91
```diff
! Infect Newly Infected !
+ Newly Infected : 0
```
```diff
! simulation_should_continue() !
+ Alive : 909
+ Dead : 91
+ Vaccinated : 909
+ Infected : 0
```
