import os
import random
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_item_color(pos):
    """Faghat range font baraye esme har khane"""
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
    markers = [" " for _ in range(40)]
    for name, data in players_data.items():
        pos = data["pos"]
        if markers[pos] == " ": markers[pos] = name
        else: markers[pos] += "+" + name

    print(f"\n{Fore.WHITE}{'='*90}")
    print(f"{' ' * 35}MONOPOLY (Admin: AmirParsa)")
    print(f"{Fore.WHITE}{'='*90}\n")

    top_line = ""
    for i in range(20, 31):
        color = get_item_color(i)
        top_line += f"|{color}{markers[i]:^7}{Style.RESET_ALL}"
    print(top_line + "|")
    print("-" * 89)

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
    bottom_line = ""
    for i in range(10, -1, -1):
        color = get_item_color(i)
        bottom_line += f"|{color}{markers[i]:^7}{Style.RESET_ALL}"
    print(bottom_line + "|")

    print(f"\n{Fore.BLACK}{Back.WHITE}{' '*38} SCORE BOARD {' '*39}{Style.RESET_ALL}")
    header = f"{'NAME':<8} | {'CASH':<8} | {'POS':<8} | {'PROPERTIES'}"
    print(header)
    print("-" * 90)
    
    for name, data in players_data.items():
        props = ", ".join(data['props']) if data['props'] else "Hichi"
        print(f"{name:<8} | ${data['money']:<7} | KH-{data['pos']:<5} | {props}")
    print("-" * 90)

if __name__ == "__main__":
    from colorama import Back 
    
    current_players = {
        "P1": {"pos": 0, "money": 1500, "props": ["Park Place", "Boardwalk"]},
        "P2": {"pos": 24, "money": 1200, "props": ["Kentucky Ave"]},
        "P3": {"pos": 10, "money": 850, "props": []},
        "P4": {"pos": 39, "money": 2100, "props": ["Reading RR", "Water Works"]}
    }    
    clear_screen()
    draw_game_ui(current_players)
    print(f"\n{Fore.YELLOW}Dastoor: {Fore.WHITE}Baraye 'Dice Roll' Enter bezanid...")