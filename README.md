# Monitor de tarefas do readmine

`$ python -m venv venv`

`$ . venv/Scripts/activate`

`$ pip install -r requirements.txt`

`$ python main.py`

`docker build --no-cache -t sysmo/n3-notification:v1 .`

`docker run -d --rm --name n3-notification sysmo/n3-notification:v1`