# **PHASE-4-SUPERHEROES-CHALLENGE BY MASUD ABDI**
#**Superheroes API**
This is a simple Flask-based API for managing superheroes and their powers. The API allows you to create, read, update, and delete superheroes and their powers.

**Getting Started**
Clone the repository:
bash
Download
Copy code
git clone[ https://github.com/masud520/superheroes-api.git](https://github.com/masud520/PHASE-4-SUPERHEROES-CHALLENGE)
cd superheroes-api
Create a virtual environment and activate it:
bash
Download
Copy code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:
bash
Download
Copy code
pip install -r requirements.txt
Run the application:
bash
Download
Copy code
flask run
Access the API at http://localhost:5000.
##**API Documentation**
1.**Heroes**
GET /heroes
Returns a list of all heroes.

GET /heroes/int:hero\_id
Returns the hero with the given ID.

POST /heroes
Creates a new hero. The request body should be a JSON object with the following properties:

name (string, required): The name of the hero.
real_name (string, required): The real name of the hero.
PUT /heroes/int:hero\_id
Updates the hero with the given ID. The request body should be a JSON object with the following properties:

name (string, optional): The new name of the hero.
real_name (string, optional): The new real name of the hero.
DELETE /heroes/int:hero\_id
Deletes the hero with the given ID.

2.**Powers**
GET /powers
Returns a list of all powers.

GET /powers/int:power\_id
Returns the power with the given ID.

POST /powers
Creates a new power. The request body should be a JSON object with the following properties:

name (string, required): The name of the power.
description (string, required): The description of the power.
PUT /powers/int:power\_id
Updates the power with the given ID. The request body should be a JSON object with the following properties:

name (string, optional): The new name of the power.
description (string, optional): The new description of the power.
DELETE /powers/int:power\_id
Deletes the power with the given ID.

Hero Powers
POST /hero_powers
Creates a new hero power. The request body should be a JSON object with the following properties:

hero_id (integer, required): The ID of the hero.
power_id (integer, required): The ID of the power.
strength (integer, required): The strength of the hero's power.
Database Models
The API uses three database models: Hero, Power, and HeroPower.

Hero
id (integer, primary key): The ID of the hero.
name (string): The name of the hero.
real_name (string): The real name of the hero.
Power
id (integer, primary key): The ID of the power.
name (string): The name of the power.
description (string): The description of the power.
HeroPower
id (integer, primary key): The ID of the hero power.
hero_id (integer, foreign key to Hero): The ID of the hero.
power_id (integer, foreign key to Power): The ID of the power.
strength (integer): The strength of the hero's power.
###**AUTHOR**
**MASUD ABDI**
