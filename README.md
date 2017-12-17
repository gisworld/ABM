# ABM Practicals
This repository houses the code from the Practical component of GEOG5991M <br>
Each Practical is stored in its own folder <br>
*Example*: If you would like to test inputting your own arguments, look in ABM/Animation/Sheep or Wolves_eat_sheep and run the models ending with argv <br>
The Final models are contained in the 2 zipped folders: <br>
## StandardABM.zip 
- The standard ABM based on the practicals. 
Sheep move around the CSV read environment until all the sheep are at least half full.
The AgentFramework uses getter and setters, overrides the str variable, enables sheep for eat, move, be sick and share with neighbours<br>
## EnhancedABM.zip 
- The enhanced model introduces Wolves to eat the sheep. The model runs until all the sheep are eaten or 200 iterations.
