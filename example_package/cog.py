import random
from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands
from tortoise.exceptions import DoesNotExist

from ballsdex.core.models import Player, BallInstance

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


class ExampleCog(commands.Cog):
    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @app_commands.command()
    async def randomball(self, interaction: discord.Interaction):
        """
        Show a random countryball of your inventory!
        """
        try:
            player = await Player.get(discord_id=interaction.user.id)
        except DoesNotExist:
            await interaction.response.send_message("You are not a registered player.")
            return

        if not await player.balls.all().exists():
            await interaction.response.send_message("You do not have any countryball yet.")
            return

        await interaction.response.defer(thinking=True)
        pk = random.choice(await player.balls.all().values_list("id"))
        ball = await BallInstance.get(pk=pk[0])
        text, file = await ball.prepare_for_message(interaction)
        await interaction.followup.send(text, file=file)

