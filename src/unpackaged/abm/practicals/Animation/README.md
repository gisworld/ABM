# Animation
This folder contains the standard model and enhanced model in 3 phases:
## Sheep folder
- model.py files allows for 100 iterations
- model_stopping_condition_argv.py files allow the user to input values in command line in the following format: Num_of_agents, Num_of_iterations, Neighbourhood
- model_stopping_condition.py files have a built in stop when sheep are half full
-- or all sheep have been eaten by wolves (in Wolves_eat_sheep folder)
-- or iterations reach 200 if sheep haven't been eaten (in Wolves_eat_sheep folder)
## Wolves eat sheep
- model.py files allows for 100 iterations
- model_stopping_condition_argv.py files allow the user to input values in command line in the following format: Num_of_agents, Num_of_wolves, Num_of_iterations, Neighbourhood
- model_stopping_condition.py files have a built in stop when sheep are all eaten or 200 iterations are reached
## Trying Tkinter
- An optional practical using tkinter as a UI to run the model from a drop down menu
