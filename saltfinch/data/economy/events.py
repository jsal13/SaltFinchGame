import random

from saltfinch.economy.events import Event, EventType


"""
Generates a list of events with their details.

Each event has a name, description, type (positive, negative, neutral), and a dictionary of resources with their respective multipliers.
"""

# POSITIVE EVENTS

positive_events: list["Event"] = []

positive_events.append(Event(
    "Bountiful Harvest", 
    "The recent harvest exceeded expectations!",
    EventType.POSITIVE,
    {"wheat": 0.4, "corn": 0.4, "potatoes": 0.4, "apples": 0.4}
))

positive_events.append(Event(
    "Trade Caravan", 
    "A merchant caravan has arrived with goods from afar.",
    EventType.POSITIVE,
    {"iron": 0.85, "cloth": 0.9, "tools": 0.85}
))

positive_events.append(Event(
    "Livestock Boom", 
    "Livestock are thriving and producing more than usual.",
    EventType.POSITIVE,
    {"milk": 0.8, "eggs": 0.75, "chicken": 0.9, "beef": 0.9, "wool": 0.8}
))

# NEGATIVE EVENTS

negative_events: list["Event"] = []

negative_events.append(Event(
    "Drought", 
    "A lack of rainfall has damaged crops.",
    EventType.NEGATIVE,
    {"wheat": 1.3, "corn": 1.3, "potatoes": 1.25, "apples": 1.2}
))

negative_events.append(Event(
    "Animal Illness", 
    "A mild illness is affecting farm animals.",
    EventType.NEGATIVE,
    {"milk": 1.2, "eggs": 1.25, "chicken": 1.15, "beef": 1.1}
))

negative_events.append(Event(
    "Mine Collapse", 
    "A partial collapse at the mine has reduced output.",
    EventType.NEGATIVE,
    {"iron": 1.4}
))

negative_events.append(Event(
    "Forest Fire", 
    "A fire has damaged part of the nearby forest.",
    EventType.NEGATIVE,
    {"lumber": 1.3}
))

negative_events.append(Event(
    "Flu Outbreak", 
    "A flu is spreading through town.",
    EventType.NEGATIVE,
    {"medicine": 1.5}
))

# NEUTRAL EVENTS
neutral_events: list["Event"] = []

neutral_events.append(Event(
    "Town Festival", 
    "The annual town festival is approaching.",
    EventType.NEUTRAL,
    {"cloth": 0.9, "apples": 1.2, "cheese": 1.1}
))

neutral_events.append(Event(
    "Season Change", 
    "The seasons are changing.",
    EventType.NEUTRAL,
    {"wool": 0.9 if random.random() > 0.5 else 1.1, 
    "lumber": 0.9 if random.random() > 0.5 else 1.1}
))


# COMBINE ALL EVENTS
ALL_EVENTS: list["Event"] = positive_events + negative_events + neutral_events