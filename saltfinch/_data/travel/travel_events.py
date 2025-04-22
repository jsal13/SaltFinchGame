from saltfinch.travel.travel_events import TravelEvent

TRAVEL_EVENTS: list["TravelEvent"] = [
    TravelEvent(
        "River Crossing",
        "You've come to a river. It looks deep and the current is strong.",
        ["Ford the river", "Look for a shallower crossing", "Build a raft"],
        [
            {
                "health": -20,
                "water": -10,
                "money": 0,
                "msg": "You ford the river but your wagon gets damaged and you lose supplies.",
            },
            {
                "health": -5,
                "water": -5,
                "money": 0,
                "msg": "You find a safer crossing but it takes extra time.",
            },
            {
                "health": -10,
                "water": -15,
                "money": -30,
                "msg": "You build a raft which helps, but it's costly and time-consuming.",
            },
        ],
    ),
    TravelEvent(
        "Wild Animals",
        "You spot a herd of buffalo in the distance.",
        ["Hunt them for food", "Keep your distance", "Try to scare them away"],
        [
            {
                "health": -10,
                "water": +50,
                "money": 0,
                "msg": "You hunt successfully but get injured in the process.",
            },
            {
                "health": 0,
                "water": -5,
                "money": 0,
                "msg": "You avoid the buffalo and continue safely, consuming a bit of food.",
            },
            {
                "health": -15,
                "water": -10,
                "money": 0,
                "msg": "The buffalo charge! You escape but sustain injuries and lose supplies.",
            },
        ],
    ),
    TravelEvent(
        "Weather",
        "Dark clouds gather on the horizon. A storm is brewing.",
        ["Push on through", "Set up camp and wait", "Find shelter"],
        [
            {
                "health": -25,
                "water": -15,
                "money": 0,
                "msg": "The storm hits hard. You're soaked and many supplies are ruined.",
            },
            {
                "health": -5,
                "water": -20,
                "money": 0,
                "msg": "You wait out the storm, staying relatively dry but using extra food.",
            },
            {
                "health": -10,
                "water": -10,
                "money": 0,
                "msg": "You find a small cave for shelter but some supplies get wet anyway.",
            },
        ],
    ),
    TravelEvent(
        "Bandits",
        "A group of suspicious men approach your wagon.",
        ["Attempt to fight them off", "Try to negotiate", "Flee immediately"],
        [
            {
                "health": -30,
                "water": -10,
                "money": -20,
                "msg": "You fend them off but get wounded in the fight and lose some valuables.",
            },
            {
                "health": -5,
                "water": -5,
                "money": -50,
                "msg": "You negotiate and give them some money to leave you alone.",
            },
            {
                "health": -15,
                "water": -25,
                "money": 0,
                "msg": "You escape but lose some supplies in your haste.",
            },
        ],
    ),
    TravelEvent(
        "Illness",
        "One of your party members has fallen ill with fever.",
        [
            "Use medicine",
            "Rest for a few days",
            "Continue and hope for the best",
        ],
        [
            {
                "health": -5,
                "water": -10,
                "money": 0,
                "msg": "The medicine helps and they recover quickly.",
            },
            {
                "health": -10,
                "water": -30,
                "money": 0,
                "msg": "Extended rest helps them recover but consumes extra food.",
            },
            {
                "health": -25,
                "water": -15,
                "money": 0,
                "msg": "Their condition worsens, affecting the whole party's morale and health.",
            },
        ],
    ),
    TravelEvent(
        "Broken Wagon",
        "Your wagon wheel has broken on the rough trail.",
        [
            "Use spare parts to fix it",
            "Try to repair it with available materials",
            "Continue with the damaged wheel",
        ],
        [
            {
                "health": 0,
                "water": -5,
                "money": 0,
                "msg": "You quickly fix the wheel with your spare parts.",
            },
            {
                "health": -5,
                "water": -15,
                "money": 0,
                "msg": "Your makeshift repair works but takes time and energy.",
            },
            {
                "health": -20,
                "water": -25,
                "money": 0,
                "msg": "The damaged wheel makes travel difficult and dangerous.",
            },
        ],
    ),
    TravelEvent(
        "Friendly Travelers",
        "You meet a friendly group of travelers heading the same direction.",
        [
            "Travel together for safety",
            "Trade supplies with them",
            "Share information but travel separately",
        ],
        [
            {
                "health": 10,
                "water": -5,
                "money": 0,
                "msg": "The company boosts morale but means more mouths to feed.",
            },
            {
                "health": 0,
                "water": 10,
                "money": -10,
                "msg": "You trade some money for additional food.",
            },
            {
                "health": 5,
                "water": -5,
                "money": 0,
                "msg": "You learn about the trail ahead, which helps your journey.",
            },
        ],
    ),
    TravelEvent(
        "Lost Trail",
        "You seem to have wandered off the main trail.",
        [
            "Backtrack to the last known point",
            "Scout ahead for landmarks",
            "Make your own path",
        ],
        [
            {
                "health": -5,
                "water": -20,
                "money": 0,
                "msg": "You safely return to the trail but lose time and consume extra food.",
            },
            {
                "health": -15,
                "water": -15,
                "money": 0,
                "msg": "Scouting is tiring but you find your way back.",
            },
            {
                "health": -25,
                "water": -30,
                "money": 0,
                "msg": "Your shortcut turns dangerous, causing injuries and consuming supplies.",
            },
        ],
    ),
]
