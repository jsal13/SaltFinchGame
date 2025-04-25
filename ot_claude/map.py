def generate_ascii_map(towns, player_position, terminal_width=80):
    """
    Generate an ASCII map showing towns and the player's current position.
    
    Args:
        towns: List of Town objects with name and distance attributes
        player_position: Current distance traveled by the player
        terminal_width: Width of the terminal display (default: 80)
    
    Returns:
        A multi-line string representing the ASCII map
    """
    # Calculate the total trail length and scale factor
    total_distance = towns[-1].distance
    scale_factor = (terminal_width - 10) / total_distance
    
    # Create the map header
    map_lines = [
        f"{'=' * terminal_width}",
        f"OREGON TRAIL MAP".center(terminal_width),
        f"{'=' * terminal_width}",
        ""
    ]
    
    # Create distance scale line
    scale_line = "0" + " " * (terminal_width - 12) + f"{total_distance} miles"
    map_lines.append(scale_line)
    
    # Generate the trail line with town markers
    trail_line = ""
    town_positions = {}
    
    # First pass: calculate town positions on the trail
    for town in towns:
        pos = int(town.distance * scale_factor) + 1  # +1 to account for the "0" at the start
        town_positions[pos] = town.name
    
    # Second pass: create the trail line
    for i in range(terminal_width):
        if i in town_positions:
            trail_line += "O"  # Town marker
        elif i == int(player_position * scale_factor) + 1:
            trail_line += "X"  # Player position
        elif i < terminal_width - 10:
            trail_line += "-"  # Trail
        else:
            trail_line += " "  # Empty space at the end
    
    map_lines.append(trail_line)
    
    # Add town names beneath their markers
    town_labels = [""] * 3  # Three lines for town labels
    current_line = 0
    
    for pos, name in town_positions.items():
        # Ensure town name will fit without overwriting another town's name
        # Try to place it on the line with the most space available
        placed = False
        for attempt in range(3):
            line_idx = (current_line + attempt) % 3
            
            # Check if there's space for this town name
            if pos + len(name) <= terminal_width:
                # Check if this position would overlap with existing text
                overlap = False
                for i in range(len(name)):
                    if pos + i < len(town_labels[line_idx]) and town_labels[line_idx][pos + i] != " ":
                        overlap = True
                        break
                
                if not overlap:
                    # Extend the line with spaces if needed
                    if len(town_labels[line_idx]) < pos:
                        town_labels[line_idx] += " " * (pos - len(town_labels[line_idx]))
                    
                    # Add the town name
                    if len(town_labels[line_idx]) == pos:
                        town_labels[line_idx] += name
                    else:
                        prefix = town_labels[line_idx][:pos]
                        suffix = town_labels[line_idx][pos + len(name):]
                        town_labels[line_idx] = prefix + name + suffix
                    
                    current_line = (line_idx + 1) % 3
                    placed = True
                    break
        
        if not placed:
            # If we couldn't place it nicely, just put it somewhere
            line_idx = current_line
            if len(town_labels[line_idx]) < pos:
                town_labels[line_idx] += " " * (pos - len(town_labels[line_idx]))
            
            if len(town_labels[line_idx]) == pos:
                town_labels[line_idx] += name
            else:
                town_labels[line_idx] = town_labels[line_idx][:pos] + name
            
            current_line = (line_idx + 1) % 3
    
    # Add the town label lines to the map
    for label_line in town_labels:
        map_lines.append(label_line)
    
    # Add legend
    map_lines.extend([
        "",
        "Legend:".ljust(terminal_width),
        "O : Town     X : Your Position     - : Trail".ljust(terminal_width),
        f"{'=' * terminal_width}"
    ])
    
    return "\n".join(map_lines)


def display_map(game):
    """
    Function to display the ASCII map in the game context.
    
    Args:
        game: The Game object containing towns and player information
    """
    # Get terminal width (fallback to 80 if can't determine)
    try:
        import shutil
        terminal_width = shutil.get_terminal_size().columns
    except (ImportError, AttributeError):
        terminal_width = 80
    
    # Cap the width to reasonable bounds
    terminal_width = max(60, min(terminal_width, 120))
    
    # Generate and print the map
    ascii_map = generate_ascii_map(
        game.towns,
        game.player.distance_traveled,
        terminal_width=terminal_width
    )
    print(ascii_map)


# Example integration with your game class:
"""
# Add this method to your Game class:

def show_map(self):
    self.clear_screen()
    display_map(self)
    input("\nPress Enter to continue...")

# Then modify handle_town_options() to include the map option:
def handle_town_options(self):
    town = self.towns[self.current_town_index]
    
    while True:
        self.show_status()
        print(f"Welcome to {town.name}!")
        print("\nWhat would you like to do?")
        print("1. Buy supplies")
        print("2. Rest and heal")
        print("3. View map")
        print("4. Continue your journey")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            self.buy_supplies(town)
        elif choice == "2":
            self.rest_and_heal()
        elif choice == "3":
            self.show_map()
        elif choice == "4":
            if self.current_town_index == len(self.towns) - 1:
                self.game_won()
                return
            return  # Exit town and continue journey
        else:
            print("Invalid choice. Please try again.")
"""


# Example usage as a standalone script
if __name__ == "__main__":
    # Test the map with example data
    class TownExample:
        def __init__(self, name, distance):
            self.name = name
            self.distance = distance
    
    class PlayerExample:
        def __init__(self):
            self.distance_traveled = 500
    
    class GameExample:
        def __init__(self):
            self.towns = [
                TownExample("Independence", 0),
                TownExample("Fort Kearney", 250),
                TownExample("Fort Laramie", 500),
                TownExample("Fort Bridger", 750),
                TownExample("Fort Hall", 1000),
                TownExample("Fort Boise", 1200),
                TownExample("Fort Walla Walla", 1400),
                TownExample("Oregon City", 1600)
            ]
            self.player = PlayerExample()
    
    game_example = GameExample()
    display_map(game_example)
    input("\nPress Enter to exit...")