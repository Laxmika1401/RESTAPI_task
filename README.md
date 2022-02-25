# TVA_task
This is a REST API for fetching the user details from database using Django Rest Framework. 
METHOD	ROUTE	FUNCTIONALITY	ACCESS
POST	/auth/signup/	Register new user	All users
POST	/auth/jwt/create/	Login user	All users
POST	/auth/jwt/refresh/	Refresh the access token	All users
POST	/auth/jwt/verify/	Verify the validity of a token	All users
POST	/orders/	Place an order	All users
POST	/orders/	Get all orders	All users
GET	/order/{order_id}/	Retrieve an order	Superuser
PUT	/orders/{order_id}/	Update an order	All users
PUT	/update-status/{order_id}/	Update order status	Superuser
DELETE	/delete/{order_id}/	Delete/Remove an order	All users
GET	/user/{user_id}/orders/	Get user's orders	All users
GET	/user/{user_id}/order/{order_id}/	Get user's specific order	
GET	/docs/	View API documentation	All users
