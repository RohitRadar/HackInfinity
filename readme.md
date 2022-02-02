## SSN Hackfinity 2021 
Our solution for SSN Invente 2021's Hackathon. To help maitain godowns in a pristine and safe condition using raspberry pi.
### mysite
Django Website hosted on raspberry pi to monitor sensor values and view livestream of cameras.
### surveillance
Python Code to Stream Camera
### HackInfinity.ipynb
ML Model to detect fires/rodents/pests in the godown

### Implementation
### Pest Detection:
Pests and rodents give off heat signatures whereas the harvest does not. Infrared Sensors are used to detect pests rodents and store footage of the heat signatures so that authorities can take preventive measures, understand where they come from and take pest control measures. Knowing where they enter and exit from the godown can be valuable information as these points of entry can be sealed and traps can be placed to deter their entry. 

### Grain Condition Detection:
The camera module can be used to get live footage inside the storage facility. The crops can be monitored 24/7. Routinely the grain and vegetable images can be fed though an ML model to detect if there are any diseases or signs of rot. Public 
Datasets of healthy harvest and damaged grains can be used to create an ML modelwhich can predict if there are signs of damage in the harvest. If damage has been detected, the godown manager can be alerted using a locally hosted website dashboard so that they can remove those diseased produce from the fresh healthy produce.

### Environment Sensors:
Humidity Sensors, Temperature Sensors, Smoke Sensors are required to get real time condition inside godown. Temperature and Humidity sensors can be used to detect the condition. If the conditions do not satisfy the optimal storage levels, the
automatic hardware systems can be enabled to get to optimal storage conditions.Fans can be used to reduce the temperature and get fresh air into the storage room. Humidity can be reduced using a dehumidifier.
