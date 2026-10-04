import nextcord

from nextcord import Interaction, SlashOption
from nextcord.ext.commands import Bot, Cog
from componentsv2 import NextcordAPIWrapperV2 as Wrapper

from Utils.Components.log_components import LogModal

class LogGroup(Cog):
    def __init__(self, bot: Bot, wrapper: Wrapper):
        self.wrapper = wrapper
        self.bot = bot

    @nextcord.slash_command(name="log", description="All case log-related commands.")
    async def log(self, interaction):
        pass

    @log.subcommand("create", description="Create a case log to be reviewed by other Scam Investigators.")
    async def log_create(self, interaction: Interaction, investigator: nextcord.Member = SlashOption(
        name="investigator",
        description="The scam investigator who originally conducted this investigation (defaults to you).",
        required=False
    ), notes: str = SlashOption(
        name="notes",
        description="Notes/links that apply to this case.",
        required=False
    )):
        await self.wrapper.send_modal(interaction, LogModal(interaction, self.wrapper, investigator=investigator, notes=notes))

def setup(bot: Bot, **kwargs):
    bot.add_cog(LogGroup(bot, kwargs.get("wrapper")))