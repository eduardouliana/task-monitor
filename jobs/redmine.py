from utils.postgresql import Postgresql
from utils.discord import Discord
import configparser

class Redmine:
    _config = configparser.ConfigParser()
    _config.read('config.ini')
    
    __REDMINE_SECTION = 'REDMINE'
    __DISCORD_WEBHOOK = 'DISCORD'

    __HOST = _config[__REDMINE_SECTION]['host']
    __DATABASE = _config[__REDMINE_SECTION]['database']
    __USER = _config[__REDMINE_SECTION]['user']
    __PASS = _config[__REDMINE_SECTION]['password']
    __URL = _config[__REDMINE_SECTION]['url']
    __WEB_HOOK = _config[__DISCORD_WEBHOOK]['webhook']

    def __getN3Tasks(self):
        __command = """
            select 
                upper(pri.name),                
                tsk.subject,
                tsk.id
            from 
                issues tsk 
            inner join enumerations pri on pri.id = tsk.priority_id and pri."type" = 'IssuePriority'
            where 
                tsk.assigned_to_id = 193 and 
                tsk.closed_on is null
            order by tsk.priority_id desc
        """

        return Postgresql().getExecuteQuery(
            self.__HOST, 
            self.__DATABASE, 
            self.__USER, 
            self.__PASS, 
            __command
        )

    def sendN3TasksNotification(self):
        tasks = self.__getN3Tasks()

        if len(tasks) == 0:
            return

        description = ''  
        
        for task in tasks:
            taskPriority = task[0]
            taskDescription = task[1]
            taskId = task[2]

            description = f'''
                {description}
                :point_right: **[{taskPriority}]** - {taskDescription} 
                {self.__URL}/issues/{taskId}
            '''
        Discord().sendNotification(self.__WEB_HOOK, f'Quantidade de tarefas no N3: [ {len(tasks)} ]  :fire:', description)
        
    def getTaskStatus(self, taskId):
        __command = f"""
            select
                cast(cast(closed_on as date) as text) 
            from
                issues t
            inner join issue_statuses s on
                s.id = t.status_id 
            where t.id = {taskId}
            and closed_on is not null            
        """

        return Postgresql().getExecuteQuery(
            self.__HOST, 
            self.__DATABASE, 
            self.__USER, 
            self.__PASS, 
            __command
        )
