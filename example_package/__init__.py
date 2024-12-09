from typing import TYPE_CHECKING

from example_package.cog import ExampleCog

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


async def setup(bot: "BallsDexBot"):
    await bot.add_cog(ExampleCog(bot))

