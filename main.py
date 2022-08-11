import interactions as dc
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = dc.Client(DISCORD_TOKEN)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.me.name} ({bot.me.id})")
    await bot.change_presence(dc.ClientPresence(activities = [dc.PresenceActivity(name = "command /nose", type = dc.PresenceActivityType.GAME)]))

@bot.command(
    name = "nose",
    description = "Initiate or participate in a game of nose goes with the members of your voice channel"
)
async def nose(ctx: dc.CommandContext):
    pass
    # TODO

if __name__ == "__main__":
    bot.start()