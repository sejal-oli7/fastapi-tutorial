## Introdution to FastAPI

## strp 1:
- create a repo
- create .venv (use uv package manager)
- install fastapi
- install unicorn[standard]

##step 2:
- create a file name as main.py
- add a GET endpoint and create a funtion for Welcome to fast api tutorial

## step 3:
- run the server using uvicorn:
'''uvicorn main:app --reload'''

# Command used for Univcorn main:app
'''host (bind socket to this host)'''
'''port (default 8000)'''
'''reload (enable auto reload)'''
'''version (it displays uvicorn version)'''
'''help (show the message & exit)'''


### starting uvicorn server from the program itself

### Path parameters

- e.g ```http://localhost:8000/hello/elevatex```

this path ```/hello/elevatex```we call it as path or route.

### Method and Parameters
- GET sends data in unencrypted form to the server. Most common method method.

- POST : Send html form data to the server and then recieve the data from the server.

-PUT : Replaces all the current representation of the target resources with uploaded content.

- PATCH : Partial resources update.

- DELETE : Removes all current representation of the target sources given by URL. When i delete anything from the system, from the backend side, we change the status flag(active/inactive) of nay field.


e.g sejal emp delete meaning, in the database, i will archive emp sejal from the backend, changing the status to inactive.

### Async Keyword:
- Itmeans without blocking the current thread of execution 
