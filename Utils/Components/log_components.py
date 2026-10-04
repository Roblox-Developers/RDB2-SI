from nextcord import Interaction, TextInputStyle, Member
from nextcord.ext.commands import Bot

from componentsv2 import (
    ModalV2, 
    NextcordAPIWrapperV2 as Wrapper,

    UserSelect,
    StringSelect,

    DefaultValue,

    TextInput,

    Label,
)

## MODAL CLASSES
class LogModal(ModalV2):
    def __init__(self, interaction: Interaction, wrapper: Wrapper, *, investigator: Member = None, notes: str = None):
        super().__init__("Create Case Log", timeout=600, custom_id="create_log")
        self.wrapper = wrapper

        investigator_id = investigator.id if investigator is not None else interaction.user.id

        default_investigator = []
        default_investigator.append(DefaultValue(
            investigator_id,
            "user"
        ))
        
        self.accused = UserSelect(custom_id="accused", placeholder="Select a user...", required=True, max_values=10)
        self.investigator = UserSelect("investigator", default_investigator, "Select a user...", required=True)

        self.descriptors = StringSelect("descriptors", [
            StringSelect.SelectOption( ## add modular select options for reasons added to the guildconfig
                "A1.",
                "a1",
                "A user explodes the other party's pancakes with their mind.",
            )
        ], "Select appropriate reason codes...", required=True) ## add modular max_values up to 10 (discord limitation)

        self.punishment = TextInput(
            "punishment",
            TextInputStyle.short,
            max_length=50,
            placeholder="\"e.g., Permanent Ban\"",
            required=True,
        )

        self.notes = TextInput(
            "notes", 
            TextInputStyle.paragraph, 
            max_length=2500, 
            required=False, 
            set_value=notes, 
            placeholder="Add related links/give context."
        )

        self.add_components(
            Label("Accused User(s)", self.accused),
            Label("Case Descriptors", self.descriptors),
            Label("Punishment", self.punishment),
            Label("Investigator", self.investigator),
            Label("Additional Notes", self.notes)
        )

    async def on_form_submit(self, interaction: Interaction):
        await interaction.response.send_message(f"Accused: {self.accused.values}\nDescriptors: {self.descriptors.values}\nPunishment: {self.punishment.value}\nInvestigator: {self.investigator.value}\nNotes: {self.notes.value or "NONE!"}", ephemeral=True)