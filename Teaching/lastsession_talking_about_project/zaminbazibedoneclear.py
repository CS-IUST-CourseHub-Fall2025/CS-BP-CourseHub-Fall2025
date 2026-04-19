import os
import time
import random
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

# Initialize Colorama
init(autoreset=True)

def get_item_color(pos):
    """Rang-bandi baraye namayeshe esme khane-ha (Fingilish)"""
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

def generate_board(players_data):
    """Sakhte zamime bazi ba format-e darsat baraye Rich"""
    markers = [" " for _ in range(40)]
    for name, data in players_data.items():
        pos = data["pos"]
        if markers[pos] == " ": markers[pos] = name
        else: markers[pos] += "+" + name

    res = ""
    # TOP ROW
    line = ""
    for i in range(20, 31):
        c = get_item_color(i)
        line += f"|{c}{markers[i]:^5}{Style.RESET_ALL}"
    res += line + "|\n" + "-" * 67 + "\n"

    # MIDDLE
    for i in range(1, 10):
        l_idx, r_idx = 20 - i, 30 + i
        l_c, r_c = get_item_color(l_idx), get_item_color(r_idx)
        res += f"|{l_c}{markers[l_idx]:^5}{Style.RESET_ALL}|{' '*53}|{r_c}{markers[r_idx]:^5}{Style.RESET_ALL}|\n"
        if i < 9: res += "-" * 7 + " " * 53 + "-" * 7 + "\n"

    # BOTTOM
    res += "-" * 67 + "\n"
    line = ""
    for i in range(10, -1, -1):
        c = get_item_color(i)
        line += f"|{c}{markers[i]:^5}{Style.RESET_ALL}"
    res += line + "|"
    return res

def get_score_table(players_data):
    """Sakhte Scoreboard ba Rich Table"""
    table = Table(box=None, expand=True)
    table.add_column("Player", style="bold cyan", justify="center")
    table.add_column("Cash", style="green", justify="right")
    table.add_column("Position", style="yellow", justify="center")
    table.add_column("Assets", style="magenta", justify="left")

    for name, data in players_data.items():
        assets = ", ".join(data['props']) if data['props'] else "None"
        table.add_row(name, f"${data['money']}", f"Khane {data['pos']}", assets)
    return table

def main():
    players = {
        "P1": {"pos": 0, "money": 1500, "props": ["Park Place"]},
        "P2": {"pos": 10, "money": 1200, "props": []}
    }
    
    console = Console()
    
    with Live(console=console, screen=False, refresh_per_second=4) as live:
        for _ in range(15):
            # Mantegh-e Harekat
            for p in players:
                players[p]["pos"] = (players[p]["pos"] + random.randint(1, 6)) % 40
                players[p]["money"] += random.choice([-50, 100, 0])

            # Sakhte mohtavaye nahayi baraye namayesh
            board_text = generate_board(players)
            score_table = get_score_table(players)
            
            # Jam kardan-e har do dar yek Panel
            combined_content = f"{board_text}\n\n"
            final_ui = Panel(combined_content, title="[bold yellow]MONOPOLY TERMINAL[/bold yellow]", subtitle="Admin: AmirParsa")
            
            # Update kardan-e Live
            console.clear() # Pak kardan baraye jologiri az tahrir-e ezafe
            live.update(final_ui)
            console.print(score_table) # Scoreboard ro zir-e panel chap mikonim
            
            time.sleep(1)

if __name__ == "__main__":
    main()