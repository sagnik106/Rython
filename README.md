# Rython
A [dicord bot](https://discordapp.com/oauth2/authorize?client_id=705275933912989736&scope=bot&permissions=67584) to run R commands in the designated text channel.
## Bot Link
https://discordapp.com/oauth2/authorize?client_id=705275933912989736&scope=bot&permissions=67584
## Requirements
* Python 3.8
* discord.py 1.0.0
* rpy2 3.3.2
* R 3.6.3
* Flask 1.1.1 (If you want it to be hosted on a server)
* Linux 5.4.0 (If you want it to be hosted on a server)
* Docker 19.03.8 (If you want it to be hosted on a server)

## File Architecture
[bot.py](https://github.com/sagnik106/Rython/blob/master/bot.py) - Running this script will get the bot up and alive</br>
[server.py](https://github.com/sagnik106/Rython/blob/master/server.py) - Flask application to keep the server in running state</br>
[Dockerfile](https://github.com/sagnik106/Rython/blob/master/Dockerfile) - Dockerfile</br>
[runner.sh](https://github.com/sagnik106/Rython/blob/master/runner.sh) - Runs both the python files for the environment

## Running the project
### On local machine
```python3 bot.py```</br>
or</br>
```./runner.sh```
### On server
Run the docker image