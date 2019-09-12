# Django Rest API - WishList LuizaLabs
---

API made as part of the process of LuizaLabs evaluation

---
## Requirements
---
- [docker-compose](https://docs.docker.com/compose/install/)

## Run the Project

---
### Setup
---
Start by cloning the project
> ```$ git clone https://github.com/LucasSRocha/django_rest_llabs.git```

Enter the project
folder
> ```$ cd django_rest_llabs```

Build the docker image
> ```$ docker-compose build```

Start the docker
> ```$ docker-compose up```

Alternatively
you can build the docker image and run it in a single command
> ```$ docker-compose up --build```

### Acessing the docker shell
You can access the image shell to further
manipulate it
> ```$ docker-compose exec api_web sh```

### Creating a super user

Inside the api_web shell
> ```$ python manage.py createsuperuser```

You'll be prompted for a username, e-mail and a password.

### UserMagalu  - Endpoint_allowed_methods(GET, POST, PATCH, DELETE)
This will use our ```api/usermagalu/``` endpoint

> ```$ curl -d "username=usuario teste&email=email.teste@gmail.com" -X POST http://localhost:8000/api/usermagalu/```

```{.python .input  n=1}
!curl -d "username=usuario teste&email=email.teste@gmail.com" -X POST http://localhost:8000/api/usermagalu/
```

```{.json .output n=1}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{\"username\":\"usuario teste\",\"email\":\"email.teste@gmail.com\"}"
 }
]
```

### Getting JWT Auth Token - Endpoint_allowed_methods(POST)
The authentication used to modify the API objects is JWT Token and it's obtained though a endpoint
**required_fields {"email": "< USER_EMAIL >", "password": "< USERNAME >"}**

>
```$ curl -d "password=usuario teste&email=email.teste@gmail.com" -X POST http://localhost:8000/api/auth/login/```
>```{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6Imx1Y2FzLmdtYWlsQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0NDI1MywiZW1haWwiOiJsdWNhcy5nbWFpbEBnbWFpbC5jb20ifQ.fYnEi083f246L0nXHqfOv8j6G8pUBGCdAR-eXsgtW90"}```

To be able to access the informations you have to pass the auth token in the headers sections of your request

```{.python .input  n=12}
!curl -d "password=usuario teste&email=email.teste@gmail.com" -X POST http://localhost:8000/api/auth/login/
```

```{.json .output n=12}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{\"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImVtYWlsLnRlc3RlQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0ODMwMiwiZW1haWwiOiJlbWFpbC50ZXN0ZUBnbWFpbC5jb20ifQ.2qI4X0aXTbn4Al-6o33kKD2lWpk6fm09-xQCUk9QY6A\"}"
 }
]
```

```{.python .input  n=4}
!curl -X GET http://localhost:8000/api/
```

```{.json .output n=4}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{\"detail\":\"Authentication credentials were not provided.\"}"
 }
]
```

```{.python .input  n=9}
!curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImVtYWlsLnRlc3RlQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0NzA0MiwiZW1haWwiOiJlbWFpbC50ZXN0ZUBnbWFpbC5jb20ifQ.YNTMfbiq6Ie1SY_LGju_Wbz8n9gl0AgY96cbr-3gXX0"  -X GET http://localhost:8000/api/
```

```{.json .output n=9}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{\"usermagalu\":\"http://localhost:8000/api/usermagalu/\",\"wishlist\":\"http://localhost:8000/api/wishlist/\",\"product\":\"http://localhost:8000/api/product/\"}"
 }
]
```

### Wishlist - Endpoint_allowed_methods(GET, POST, PATCH, DELETE)
Using the ```/api/wishlist/``` endpoint you're able to create a wishlist for your user and name it if you want.

```{.python .input  n=10}
!curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImVtYWlsLnRlc3RlQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0NzA0MiwiZW1haWwiOiJlbWFpbC50ZXN0ZUBnbWFpbC5jb20ifQ.YNTMfbiq6Ie1SY_LGju_Wbz8n9gl0AgY96cbr-3gXX0" -d "wishlist_name=lista de favoritos" -X POST http://localhost:8000/api/wishlist/
```

```{.json .output n=10}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{\"wishlist_name\":\"lista de favoritos\",\"magalu_user\":6}"
 }
]
```

The Users are restricted to a single Wishlist per account

```{.python .input  n=11}
!curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImVtYWlsLnRlc3RlQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0NzA0MiwiZW1haWwiOiJlbWFpbC50ZXN0ZUBnbWFpbC5jb20ifQ.YNTMfbiq6Ie1SY_LGju_Wbz8n9gl0AgY96cbr-3gXX0" -d "wishlist_name=lista de favoritos" -X POST http://localhost:8000/api/wishlist/
```

```{.json .output n=11}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "[\"The User already have a WishList!\"]"
 }
]
```

### Products - Endpoint_allowed_methods(GET, POST, PATCH, DELETE)
Using the ```/api/product/``` endpoint you're able to create a wishlist for your user and name it if you want.

```{.python .input  n=13}
!curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImVtYWlsLnRlc3RlQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0ODMwMiwiZW1haWwiOiJlbWFpbC50ZXN0ZUBnbWFpbC5jb20ifQ.2qI4X0aXTbn4Al-6o33kKD2lWpk6fm09-xQCUk9QY6A" -d "product_name=produto x&product_id=4bd442b1-4a7d-2475-be97-a7b22a08a024" -X POST http://localhost:8000/api/product/
```

```{.json .output n=13}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{\"product_name\":\"produto x\",\"product_id\":\"4bd442b1-4a7d-2475-be97-a7b22a08a024\",\"wishlist\":3}"
 }
]
```

```{.python .input  n=14}
!curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImVtYWlsLnRlc3RlQGdtYWlsLmNvbSIsImV4cCI6MTU2ODI0ODMwMiwiZW1haWwiOiJlbWFpbC50ZXN0ZUBnbWFpbC5jb20ifQ.2qI4X0aXTbn4Al-6o33kKD2lWpk6fm09-xQCUk9QY6A" -d "product_name=produto x&product_id=4bd442b1-4a7d-2475-be97-a7b22a08a024" -X POST http://localhost:8000/api/product/
```

```{.json .output n=14}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "[\"The Product already exists in the Wishlist\"]"
 }
]
```

The model ensures that there's only unique products on a wishlist
