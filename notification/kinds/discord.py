from datetime import date
import textwrap
from discord_webhook import DiscordWebhook, DiscordEmbed

from models.notification_data import NotificationData
from utils.date_helper import DateHelper


class Notification:
    def __init__(self, data: NotificationData):
        self.__title = f"{data.title}{DateHelper.get_date(data.date_configuration)}"
        self.__webhook = DiscordWebhook(
            url=data.url, username=data.user_name, avatar_url=data.avatar_url
        )

    def send(self, embed):
        self.__webhook.add_embed(embed)
        self.__webhook.execute(remove_embeds=True)

    def execute(self, message):
        message_list = textwrap.wrap(message, 4000, replace_whitespace=False)

        for index, msg in enumerate(message_list):
            embed = DiscordEmbed(
                title=self.__title,
                description=msg,
                color="FF0000",
            )

            embed.set_footer(
                text=f"{index+1}/{len(message_list)}",
            )

            self.send(embed)
