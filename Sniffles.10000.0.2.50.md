# Simulation Base Information:
+ Population: 10000
+ Percent Population Vaccinated: 0.2
+ Virus Name: Sniffles
+ Virus Mortality Rate: 0.12
+ Virus Reproduction Rate: 0.5
```diff
! create_population() !
+ Vaccinated : 2000
+ Unvaccinated : 7950
+ Infected : 50
```
## Iteration : 1
+ Population Alive : 9993
+ Population Infected : 7
+ Population Dead : 7
```diff
! Infect Newly Infected !
+ Newly Infected : 1692
```
```diff
! simulation_should_continue() !
+ Alive : 9993
+ Dead : 7
+ Vaccinated : 2036
+ Infected : 1533
```
## Iteration : 2
+ Population Alive : 9837
+ Population Infected : 187
+ Population Dead : 163
```diff
! Infect Newly Infected !
+ Newly Infected : 49245
```
```diff
! simulation_should_continue() !
+ Alive : 9837
+ Dead : 163
+ Vaccinated : 3392
+ Infected : 6443
```
## Iteration : 3
+ Population Alive : 9157
+ Population Infected : 43551
+ Population Dead : 843
```diff
! Infect Newly Infected !
+ Newly Infected : 71
```
```diff
! simulation_should_continue() !
+ Alive : 9157
+ Dead : 843
+ Vaccinated : 8593
+ Infected : 564
```
## Iteration : 4
+ Population Alive : 9080
+ Population Infected : 43063
+ Population Dead : 920
```diff
! Infect Newly Infected !
+ Newly Infected : 0
```
```diff
! simulation_should_continue() !
+ Alive : 9080
+ Dead : 920
+ Vaccinated : 9075
+ Infected : 5
```
## Iteration : 5
+ Population Alive : 9080
+ Population Infected : 43058
+ Population Dead : 920
```diff
! Infect Newly Infected !
+ Newly Infected : 0
```
```diff
! simulation_should_continue() !
+ Alive : 9080
+ Dead : 920
+ Vaccinated : 9080
+ Infected : 0
```
