# Проект: Система для приема пользовательских ставок

## Описание проекта

Этот проект представляет собой систему для управления и обработки ставок на спортивные события. Система состоит из двух сервисов:

1. **Line-provider** - сервис для создания и обновления статуса события.
2. **Bet-maker** - сервис, позволяющий пользователям делать ставки на события и отслеживать их статус.

Архитектура построена по принципу **MVC (Model-View-Controller)**. В проекте используется стек технологий: **FastAPI**, **PostgreSQL**, **RabbitMQ**, а также докеризация всех компонентов через **Docker Compose**.

---

## Основные компоненты проекта

### 1. **Line-provider**

- Предоставляет ручки для создания и апдейта.
- Сохраняет события в базе данных (PostgreSQL).
- Пробрасывает события в сервис bet-maker
- 
#### Основные эндпоинты:

- **POST /events/create**: Создать событие.
- **POST /events/complete**: Завершить событие.

### 2. **Bet-maker**

- Обрабатывает ставки пользователей на события.
- Получает информацию о событиях из line-provider через **RabbitMQ**..
- Сохраняет историю ставок в базе данных (PostgreSQL).

#### Основные эндпоинты:

- **GET /events**: Возвращает список активных событий.
- **POST /bet**: Создает новую ставку.
- **GET /bets**: Возвращает историю всех ставок.

---

## Инфраструктура

Проект включает в себя:

- **PostgreSQL**: Для хранения ставок.
- **RabbitMQ**: Для асинхронного обмена сообщениями между сервисами.
- **FastAPI**: Для реализации API.
- **Docker**: Для контейнеризации сервисов.
- **Docker Compose**: Для упрощенного запуска всех компонентов.

---

## Установка и запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone <ссылка-на-репозиторий>
   cd <название-папки>
   ```

2. **Соберите и запустите контейнеры**:
   ```bash
   docker-compose up --build
   ```

3. **Сервисы будут доступны по следующим адресам**:
   - **Line-provider**: `http://localhost:8001`
   - **Bet-maker**: `http://localhost:8000`

---

## Структура проекта

- **src/**:
  - **api/**: Определение маршрутов и контроллеров.
  - **bl/**: Бизнес-логика приложения.
  - **common/**: Общие вспомогательные модули.
  - **db/**: Работа с базой данных.
  - **rpc/**: Взаимодействие с RabbitMQ.
  - **app.py**: Основной модуль для инициализации приложения.
  - **main.py**: Точка входа в приложение.
- **Dockerfile**: Инструкция для сборки контейнеров.
- **docker-compose.yml**: Конфигурация для управления контейнерами.

---

## Дальнейшие шаги

1. **Добавить тесты**
2. **Добавить кеширование**.
