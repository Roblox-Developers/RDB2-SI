from nextcord import Interaction, TextInputStyle
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
    def __init__(self, interaction: Interaction, wrapper: Wrapper, *, accused: int = None, investigator: int = None, links: str = None):
        default_accused = []
        default_investigator = []

        if accused is not None:
            default_accused.append(DefaultValue(
                accused,
                "user"
            ))

        if investigator is None:
            investigator = interaction.user.id

        default_investigator.append(DefaultValue(
            investigator,
            "user"
        ))
        
        self.accused = UserSelect("accused", default_accused, "Select a user...", required=True)
        self.investigator = UserSelect("investigator", default_investigator, "Select a user...", required=True, max_values=10)

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
            set_value=links, 
            placeholder="Add related links/give context."
        )

        self.add_components(
            Label("Accused User(s)", self.accused),
            Label("Case Descriptors", self.descriptors),
            Label("Punishment", self.punishment),
            Label("Investigator", self.investigator),
            Label("Additional Notes", self.notes)
        )