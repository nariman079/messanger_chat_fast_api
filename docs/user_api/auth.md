# Auth API

## User register
### POST `/api/v1/register/`
#### Request body
`application/json`
```
{
    'name': "string",
    'email': "string",
    'password': "strign"
}
```
#### Responses
#### 201
```
{
    'detail': "Вы успешно зарегистрировались. На вашу почту отправлено письмо с подтверждением"
}
```
#### 400
```
{
    "{field_name}": "{input_error}"
}
```
#### 409
```
{
    'detail': "Такой пользователь уже зарегистрирован"
}
```
***
## User login
### POST `/api/v1/login/`
#### Request body
`application/json`
#### Responses
#### 200
```
{
    "token": "{my_token}"
}
```
#### 400
```
{
    "{field_name}": "{input_error}"
}
```
м