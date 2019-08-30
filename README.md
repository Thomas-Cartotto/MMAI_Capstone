# MMAI_Capstone
Machine leaning capstone project. Goal: Predict what cannabis and recipe to prescribe a patient to provide relief to their symptoms.

This repo contains three folder that facilitate the operation of Cannjoin's digital systems.

1) First there is the Recipe Recommendation Machine Learning folder. This contains sample data sets, as well as all of the jupyter
notebook files used in developmemnt. This is where new models, datastructures, and concepts are created and tested.

2) The Recipe Recommendation Python_ML API folder contains a python web app hosted through Heroku. This web app takes all the learnings
from the dev playground and condences the Machine Learning code to the final solution. This is then deployed on the server so 
Cannjoin's system across the board can access ML functions over an https connection.

3) The Recipe Recommendation  Node API folder contains all the code for the javascript API that facilitates user/database management.
This API is hosted through Google's Firebase system and provides Cannjoin's systems with endpoints to fetch data, manage users, and
add data like reviews, recipes, and strain.

All of these three main pilars interact with our custom document based databse to store user and company data. The database has
several autonomous scripts that work in the backgroun to process inbound reviews, clean data, and update all machine learing models. 
