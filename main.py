import time
import click
from core.runner import Runner
from core.configuration import Configuration

def __execute(tasks, interval):
    runner = Runner(tasks)

    while True:
        runner.perform()
        time.sleep(interval * 60)

@click.group()
@click.version_option("1.0")
def cli():
    """
    TaskMonitor
    """

@cli.command("json-file")
@click.option("--interval", default=30, help="Minutos de intervalo entra as execuções")
@click.option("--file-path", default="tasks.json", help="Arquivo contendo as tasks")
def json_file(interval, file_path):
    tasks = Configuration.get_from_json_file(file_path)
    __execute(tasks, interval)

@cli.command()
@click.option("--interval", default=30, help="Minutos de intervalo entra as execuções")
@click.option("--db-name", default="task-monitor-d4715-default-rtdb", help="Nome do RealtimeDB")
@click.option("--data-path", default="/tasks", help="Caminho até as tasks no RealtimeDB")
def firebase(interval, db_name, data_path):
    tasks = Configuration.get_from_firebase(db_name, data_path)
    __execute(tasks, interval)

if __name__ == '__main__':
    cli()
