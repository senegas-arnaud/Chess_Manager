from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
from rich.table import Table
import os

console = Console()


class View_player_info:

    def player_registration(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 5)

        title = Panel(
            "[bold magenta]📋  PLAYER REGISTRATION  📋[/bold magenta]",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        console.print(Align.center(title))
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))
        console.print()

        terminal_width = console.width
        form_width = 50
        padding_left = (terminal_width - form_width) // 2

        console.print(" " * padding_left, end="")
        name = console.input("[bold yellow]📝 Enter player's name ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        surname = console.input("[bold yellow]📝 Enter player's surname ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        birthday = console.input("[bold yellow]📅 Enter date of birth (YYYY-MM-DD) ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        national_id = console.input("[bold yellow]🆔 Enter national ID ➤[/bold yellow] ")
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))

        return name, surname, birthday, national_id

    def display_error(self, text):
        console.print(Align.center(f"\n [bold red]{text}[/bold red] \n"))

    def display_success(self, text):
        console.print(Align.center(f"[bold green]{text}[/bold green] \n"))

    def display_info(self, text):
        console.print(Align.center(f"[bold blue]{text}[/bold blue] \n"))

    def display_all_players(self, players):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if not players:
            console.print(Align.center("[yellow]No players registered yet.[/yellow]"))
            input("\n[Press Enter to continue...]")
            return
        
        title = "[bold magenta]📋  ALL PLAYERS  📋[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()
        
        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        
        table.add_column("Name", justify="left", style="white", width=20)
        table.add_column("National ID", justify="left", style="white", width=20)
        table.add_column("N°", justify="center", style="yellow", width=12)
        
        for i, player in enumerate(players, 1):
            full_name = f"{player['name']} {player['surname']}"
            
            table.add_row(
                full_name,
                player['national_id'],
                str(i)
            )
        
        console.print(Align.center(table))
        console.print()
        console.print(Align.center(f"[bold cyan]Total: {len(players)} player(s)[/bold cyan]"))
        console.print()
        
        input("\n[Press Enter to going back...]")
