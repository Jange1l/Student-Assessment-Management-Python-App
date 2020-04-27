# Delivery 4 - The Eagles

## Installation
  - Install dependencies with pip  
    `$ pip install -r requirements.txt`
  - Run the server    
    `$ python manage.py runserver`  
  - Migration   
    `$ python manage.py makemigrations 'app name'`  
    `$ python manage.py migrate`  

## Apps in the project
**Project Folder:**
  - settings
  - urls
  
  
**Account App:**
  - Extended User Model
  - admin site
  
 
**Registration App:**
  - Course Model
  - Team Model
  
  
**Assessment App:**
  - Question Model
  - Answer Model
  - Result_set Model
  - Assessment Model
  
  
**Login App:**
  - home page
  - student login page
  - professor login page
  - password reset page
  - updater for sending emails


**Eval_student App:**
  - student dashboard page
  - peer assessments page :arrow_right: answer assessment page
  - completed assessments page
 
 
**Eval_professor App:**
  - professor dashboard page
  - all assessments page :arrow_right: create new assessment page
  - my courses page :arrow_right: create new course page
  - teams & students page

## Data Models
  - User Model (extends the built-in Django User Model)
  - Course Model
  - Team Model
  - Question Model
  - Answer Model
  - Result_set Model
  - Assessment Model
  
