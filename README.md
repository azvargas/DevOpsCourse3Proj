# Overview

The prediction API intends to generate accurate predictions of the price of houses in a certain area.

## Project Plan

Trello board:
https://trello.com/b/SBkJNFf2/azure-devops-course-3

The spreadsheet with the planning is included in the GitHub repo

## Instructions

### Architectural Diagram (Shows how key parts of the system work)
![https://github.com/azvargas/DevOpsCourse3Proj/screenshots/master/Architectural_diagram.drawio.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/Architectural_diagram.drawio.png?raw=true)

### Running the application
1. Open an Azure Cloud Shell window
2. Clone the project from GitHub with the following command:
   git clone https://github.com/azvargas/DevOpsCourse3Proj.git
3. Enter to the flask-sklearn folder:
   cd flask-sklearn
4. Create a Python virtual environment with the following command:
   python3 -m venv .venv
5. Activate the virtual environment:
   source .venv/bin/activate
6. Execute the make command. This will install the dependencies and run the tests for the project:
   make all
7. Type the following commans tu run the application:
   export FLASK_APP='app.py'
   flask run

### Project cloned into Azure Cloud Shell
![https://github.com/azvargas/DevOpsCourse3Proj/screenshots/master/CI_project_cloned.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_project_cloned.png?raw=true)

### Passing tests that are displayed after running the `make all` command from the `Makefile`
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_make_all.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_make_all.png)

### Output of a test run
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/Output_test_run.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/Output_test_run.png)

### Successful deploy of the project in Azure Pipelines.  
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_pipeline_completed.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_pipeline_completed.png)

### Running Azure App Service from Azure Pipelines automatic deployment
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_Azure_Web_App.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_Azure_Web_App.png)

### Successful prediction from deployed flask app in Azure Cloud Shell.
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_prediction_successful.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_prediction_successful.png)

### Output of streamed log files from deployed application
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_App_Logs.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CD_App_Logs.png)

### Output of Github Actions:
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_Actions_test.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_Actions_test.png)

### README with actions badge:
![https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_Readme_badge.png](https://github.com/azvargas/DevOpsCourse3Proj/blob/main/screenshots/CI_Readme_badge.png)


## Enhancements

Currently the app does not has a frontend. Future plans for enhancements include to add a user interface to interact with the API.

## Demo 
https://youtu.be/okc_4LRDhKc

[![Python application test with Github Actions](https://github.com/azvargas/DevOpsCourse3Proj/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/azvargas/DevOpsCourse3Proj/actions/workflows/pythonapp.yml)

[![Build Status](https://dev.azure.com/factroniccloud/DevOpsCourse3/_apis/build/status%2Fazvargas.DevOpsCourse3Proj?branchName=main)](https://dev.azure.com/factroniccloud/DevOpsCourse3/_build/latest?definitionId=1&branchName=main)
