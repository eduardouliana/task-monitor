from discord_webhook import DiscordWebhook, DiscordEmbed

class Discord:

    def sendNotification(self, url, title, message):
        webhook = DiscordWebhook(url=url, username='Chuck Norris', avatar_url='https://assets.webiconspng.com/uploads/2017/09/Chuck-Norris-PNG-Image-34465.png')
        embed = DiscordEmbed(title=title, description=message, color='FF0000')   
        webhook.add_embed(embed)
        webhook.execute()