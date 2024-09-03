# Friend API

## Get my friends
### GET `/api/v1/me/friends/`
#### Response
#### 200
```
{
    Friend fields with values
}
```
***
## Add or delete friend
### POST `/api/v1/me/friends/{friend_id}/add-friend/`
#### Response 
#### 200
```
{
    'detail': "Вы добавили друга {friend_id}"
}
```
#### 204
```
{
    'detail': "Вы удалили друга {friend_id}"
}
```

#### 404
```
{
    'detail': "Такого пользователя не существует"
}
```
#### 403
```
{
    'detail': "Вы не можете добавить друга"
}
```
***

## Start chat with fiend
### POST `/api/v1/me/friends/{friend_id}/start-chat/`
#### Responses
#### 201
```
{
    'detail': "Вы начали чат"
}
```
#### 403 
```
{
    'detail': "Вы не можете начать чат"
}
```