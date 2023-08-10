# BeamBot
___
Это мой первый telegram бот, написанный на aiogram. Я умышленно не стал редактировать структуру проекта и оставил ее первоначальной, чтобы можно было отследить мой прогресс в дальнейшем.
Я его написал с целью облегчения написания курсовой работы по расчету подкрановой балки, так как в процессе самостоятельного расчета я понял, что этот процесс можно автоматизировать и упростить себе жизнь.
___

## Установка 
### 1. Регистрация бота. 
Для этого пишем боту @BotFather команду /newbot, после этого даем боту имя и тэг. После этих действий бот отправит нам токен, который никому давать нельзя.

![image](https://github.com/ILarious/BeamBot/assets/98268609/338b85e4-6998-47f3-93ed-6d9d42fd3b43)
### 2. Клонировать репозиторий

    ```bash
    git clone https://github.com/ILarious/BeamBot
    ```

### 3. Добавить переменные окружения
Создаем файл .env в корневом репозитории проекта. В него необходимо написать строку:

    ```bash
    TOKEN_API=тут-должен-быть-ваш-токен
    ```

![image](https://github.com/ILarious/BeamBot/assets/98268609/57026c39-7cde-4454-b2cb-c641db558b33)
### 4. Активация виртуального окружение
Как это сделать вы можете ознакомиться в этой статье: https://pythonchik.ru/okruzhenie-i-pakety/virtualnoe-okruzhenie-python-venv
### 5. Установить зависимости
После создания и активации виртуального окружения, чтобы установить все зависимости, в консоль прописываем 

    ```bash
    pip install -r requarement.txt
    ```
    
___
## Запуск
#### 1. Запускаем файл main.py через IDE или консоль.
    ```bash
    python3 main.py
    ```
#### 2. Переходим по ссылке к вашему боту (ссылка на бота находится в переписке с @BotFather) и пользуемся. 
