## TVA_task
This is a REST API for fetching the user details from database using Django Rest Framework. 

## Routes To Implement

| METHOD | ROUTE | FUNCTIONALITY |DATA|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/users/``` | _Get all user_| _All users_|
| *GET* | ```/api/users?page=1&limit=10&name=James&sort=-age``` | _Get user according to the requirenment_|_Selected users_|
| *POST* | ```/api/users/``` | _create new user_|_create new users_|
| *GET* | ```/api/users/{id}``` | _Retrieve an user_|_Selected user_|
| *PUT* | ```/api/users/{id}``` | _Update an user_|_selected users_|
| *DELETE* | ```/api/users{id}``` | _Delete/Remove an user_ |_selected users_|
