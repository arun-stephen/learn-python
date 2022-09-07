## Developing API using Fast-API package in Python 
This is the sample project to develop the api in python language by using fast-api.
Some characteristics of the project as follows
 - The data was maintained in-memory so, restarting the application will lose the data
 - uvicorn server will manage all api requests by exposing http url
 - The all curd operation will be performed 
 - Use Postman or any Rest API tools for validating the API request and responses

### Development Guide
 - The all required dependency of this project was defined in requirement.txt file.
So, first we need to install all required python packages by executing the below command
    > pip install -r requirement.txt
 
 - If you have modified the python package then you need to update the dependency of this project 
to requirement.txt file then execute the below command
    > pip freeze > requirement.txt

 - If you want to run the server then, execute the below command
    > uvicorn app.main:app
   
 - If you are going to working this project as development mode then, execute the below command
    > uvicorn app.main:app --reload

 - Shutdown the application by simply press `Ctrl+C` command

 - Once the server is started then,
    - API can be accessed through [http://127.0.0.1:8000/](http://127.0.0.1:8000/) url
    - swagger api documentation can be accessed through [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) url
    - redoc api documentation can be accessed through [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) url

### API Documentation
S.No|API Method|API URL| Description
-----|----------|--------------|------------------
1    | GET      | http://127.0.0.1:8000/emp/       | Retrieving all employee list
2    | GET      | http://127.0.0.1:8000/emp/{:id}  | Retrieving the employee details which matches his employee id
3    | POST     | http://127.0.0.1:8000/emp/       | Create a new employee details
4    | PUT      | http://127.0.0.1:8000/emp/{:id}  | Update a specific employee details which matches his employee id
5    | DELETE   | http://127.0.0.1:8000/emp/{:id}  | Remove the employee from the list
