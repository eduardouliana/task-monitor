from discord_webhook import DiscordWebhook, DiscordEmbed

class Notification():
    def __init__(self, data):
        self.__title = data['title']
        self.__webhook = DiscordWebhook(url=data['url'], username=data['user-name'], avatar_url=data['avatar-url'])

    def send(self, embed):
        self.__webhook.add_embed(embed)
        self.__webhook.execute()

    def execute(self, message):
        embed = DiscordEmbed(title=self.__title, description=message, color='FF0000')
        self.send(embed)
