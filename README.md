# TelegramFileURLBot
Telegram Bot (Client API) that generates a link for a file (and vice versa)

Client API : [telethon](https://github.com/LonamiWebs/Telethon)  
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API as a user or through a bot account (bot API alternative)

## Getting started

### Python 3 / Pypy3

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Run script
```bash
python client_bot.py
```

*Be careful to use Python3.X or PyPy3.X, not Python2.X* 

### Heroku

1. Download or clone this repository
2. Register on [Heroku](https://www.heroku.com/)
3. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
4. Download and install [git](https://git-scm.com/downloads)
5. On Heroku website, create a new app
6. Open terminal

   1. Login on Heroku
   
       ```bash
       heroku login
       ```

   2. Clone the project and jump into it

      ```bash
      git clone https://github.com/kernoeb/TelegramFileURLBot
      cd TelegramFileURLBot
      ```

   3. Create a new Git repository, replace <NAMEOFYOURPROJECT> with your project name (yep)

      ```bash
      git init
      heroku git:remote -a <NAMEOFYOURPROJECT>
      ```      

   4. Deploy your app

      ```bash
      git add *
      git commit -m "initial commit"
      git push heroku master
      ```

    5. Run a worker

        ```bash
        heroku ps:scale worker=1
        ```

    6. You can check your logs

        ```bash
        heroku logs --tail
        ```
