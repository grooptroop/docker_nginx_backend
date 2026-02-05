## Данная программа представляет собой демонстрацию работы простого backend‑сервиса на Python за nginx‑reverse‑proxy в Docker‑окружении.

### Список использованных технологий
- Docker
- Docker Compose
- Python
- Nginx
- Docker Network
- Healtcheck 
---

## Инструкция по запуску


#### 1. Перейти в папку, куда хотите установить проект
```bash
cd <ваша_папка>
```
#### 2. Клонировать репозиторий
```bash
git clone https://github.com/grooptroop/docker_nginx_backend.git
```
#### 3. Перейти в каталог проекта
```bash
cd docker_nginx_backend
```
#### 4. Собрать и запустить контейнеры в фоне
```bash
docker compose up --build -d
```
#### 5. Проверить работу приложения
```bash
curl http://localhost
```

---
## Описание архитектуры 

### Как поднимаются контейнеры

<img width="700" height="380" alt="image" src="https://github.com/user-attachments/assets/d28b94dc-91f6-4468-b948-7c9cb10acee1" />

1. Запускается `docker compose up --build -d`
2. Compose читает `docker-compose.yml` видит два сервиса: `backend` и `nginx`, и что nginx зависит от backend через `depends_om`
3. Сначала создаётся контейнер backend, билдится образ из `./backend/Dockerfile`, контейнер старутет и начинает слушать порт 8080 внутри своей сети 
4. Docker переодически запускает healthcheck, проверяя состояние, если команда завершилась с кодом ноль 3 итерации, то создаётся контейнер nginx


### Как обрабатывается запрос

<img width="1411" height="383" alt="image" src="https://github.com/user-attachments/assets/2cc4a714-05ba-4d53-9e17-ac4fdeb5260b" />


1. Клиент открывает соединение на `localhost:80`, это попадает в контейнер nginx
2. Nginx принимает запрос и открывает внутренее соединение к backend по адрессу `backend:8080`
3. Backend получает запрос на 8080, форимирует HTTP-ответ и записывает его в соединение `nginx-backend:8080`(Он не знает про nginx и его порты)
4. Nginx читает ответ от backend и по исходному соединению `nginx:80-клиент` отправляет ответ
5. Для клиента вся цепочка выглядит как один сервер на `localhost:80`, а внутренняя проксировка на `backend:8080` полностью скрыта внутри docker сети.
