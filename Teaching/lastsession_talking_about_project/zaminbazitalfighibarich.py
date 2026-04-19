import os
import random
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_item_color(pos):
    """Rang-e font baraye esme har khane (Board)"""
    if pos in [1, 3]: return Fore.RED 
    if pos in [6, 8, 9]: return Fore.CYAN 
    if pos in [11, 13, 14]: return Fore.MAGENTA 
    if pos in [16, 18, 19]: return Fore.YELLOW 
    if pos in [21, 23, 24]: return Fore.LIGHTRED_EX 
    if pos in [26, 27, 29]: return Fore.LIGHTYELLOW_EX 
    if pos in [31, 32, 34]: return Fore.GREEN 
    if pos in [37, 39]: return Fore.BLUE 
    if pos in [5, 15, 25, 35]: return Fore.WHITE 
    return Fore.LIGHTWHITE_EX

def draw_game_ui(players_data):
    # --- Logic-e Board (Haman kode khodet) ---
    markers = [" " for _ in range(40)]
    for name, data in players_data.items():
        pos = data["pos"]
        if markers[pos] == " ": markers[pos] = name
        else: markers[pos] += "+" + name

    print(f"\n{Fore.WHITE}{'='*90}")
    print(f"{' ' * 35}MONOPOLY (Admin: AmirParsa)")
    print(f"{Fore.WHITE}{'='*90}\n")

    # Top Row
    top_line = ""
    for i in range(20, 31):
        color = get_item_color(i)
        top_line += f"|{color}{markers[i]:^7}{Style.RESET_ALL}"
    print(top_line + "|")
    print("-" * 89)

    # Middle Section
    for i in range(1, 10):
        left_idx = 20 - i
        right_idx = 30 + i
        l_col = get_item_color(left_idx)
        r_col = get_item_color(right_idx)
        mid_space = " " * 71
        print(f"|{l_col}{markers[left_idx]:^7}{Style.RESET_ALL}|{mid_space}|{r_col}{markers[right_idx]:^7}{Style.RESET_ALL}|")
        if i < 9:
            print("-" * 9 + " " * 71 + "-" * 9)

    print("-" * 89)
    # Bottom Row
    bottom_line = ""
    for i in range(10, -1, -1):
        color = get_item_color(i)
        bottom_line += f"|{color}{markers[i]:^7}{Style.RESET_ALL}"
    print(bottom_line + "|")

    # --- Bakhsh-e jadid: Rich Scoreboard ---
    console = Console()
    
    # Sakht-e jadval ba Rich
    table = Table(title="[bold white]GAME SCOREBOARD[/bold white]", title_justify="center", border_style="blue", expand=True)
    
    table.add_column("NAME", justify="center", style="bold cyan")
    table.add_column("CASH", justify="center", style="green")
    table.add_column("POS", justify="center", style="yellow")
    table.add_column("PROPERTIES", justify="left", style="magenta")

    for name, data in players_data.items():
        props = ", ".join(data['props']) if data['props'] else "Hichi"
        table.add_row(name, f"${data['money']}", f"KH-{data['pos']}", props)

    print("\n") # Fasele az board
    console.print(table)

if __name__ == "__main__":
    current_players = {
        "P1": {"pos": 0, "money": 1500, "props": ["Park Place", "Boardwalk"]},
        "P2": {"pos": 24, "money": 1200, "props": ["Kentucky Ave"]},
        "P3": {"pos": 10, "money": 850, "props": []},
        "P4": {"pos": 39, "money": 2100, "props": ["Reading RR", "Water Works"]}
    }    
    
    clear_screen()
    draw_game_ui(current_players)
    print(f"\n{Fore.YELLOW}Dastoor: {Fore.WHITE}Baraye 'Dice Roll' Enter bezanid...")