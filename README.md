# Monitor de tarefas do readmine

`$ python -m venv venv`

`$ . venv/Scripts/activate`

`$ pip install -r requirements.txt`

`$ python main.py`

# Utilizando Doker

### Compilar
`docker build --no-cache -t sysmo/n3-stack-notification:v1 .`

### Exportar
`docker save sysmo/n3-stack-notification -o sysmo-n3-stack-notification.tar`

### Importar
`docker load -i sysmo-n3-stack-notification.tar`

### Executar
`docker run -d --rm --name n3-stack-notification sysmo/n3-stack-notification:v1`