from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import box
import os

console = Console()


class View_menu:

    def display_main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 3)

        title = Panel(
            "[bold magenta]♟️   CHESS TOURNAMENT MANAGER  ♟️[/bold magenta]",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        console.print(Align.center(title))
        console.print()

        table = Table(
            show_header=False,
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column(justify="center", style="cyan", width=10)
        table.add_column(justify="center", style="white", width=30)

        table.add_row("", "")
        table.add_row("1", "📋  Manage Players 📋")
        table.add_row("", "")
        table.add_row("", "")
        table.add_row("2", "🏆  Manage Tournaments 🏆")
        table.add_row("", "")
        table.add_row("", "")
        table.add_row("3", "📊  Reports 📊")
        table.add_row("", "")
        table.add_row("", "")
        table.add_row("0", "🚪  Exit 🚪")
        table.add_row("", "")

        console.print(Align.center(table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        while choice not in ["0", "1", "2", "3"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()

        return choice

    def display_players_menu(self, players):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = "[bold magenta]👥  MANAGE PLAYERS  👥[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        console.print(Align.center(f"[bold yellow]Total: {len(players)} player(s)[/bold yellow]"))
        console.print()

        if players:
            table = Table(
                show_header=True,
                header_style="bold magenta",
                border_style="blue",
                box=box.ROUNDED,
                expand=False
            )

            table.add_column("Full Name", justify="left", style="white", width=35)
            table.add_column("National ID", justify="center", style="yellow", width=15)
            table.add_column("Birthday", justify="center", style="green", width=15)

            for player in players:
                full_name = f"{player['name']} {player['surname']}"
                table.add_row(
                    full_name,
                    player['national_id'],
                    player['birthday']
                )

            console.print(Align.center(table))
        else:
            console.print(Align.center("[bold yellow]No players registered yet.[/bold yellow]"))

        console.print()

        menu_table = Table(
            show_header=False,
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        menu_table.add_column(justify="center", style="white", width=25)
        menu_table.add_column(justify="center", style="white", width=25)
        menu_table.add_column(justify="center", style="white", width=25)

        menu_table.add_row(
            "[cyan]1 ➤  [/cyan]Add new player",
            "[cyan]2 ➤  [/cyan]Modify player",
            "[cyan]3 ➤  [/cyan]Go back")

        console.print(Align.center(menu_table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        while choice not in ["1", "2", "3"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()

        return choice

    def display_tournaments_menu(self, tournaments):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = "[bold magenta]🏆  MANAGE TOURNAMENTS  🏆[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        console.print(Align.center(f"[bold cyan]Total: {len(tournaments)} tournaments[/bold cyan]"))
        console.print()

        if tournaments:
            table = Table(
                show_header=True,
                header_style="bold magenta",
                border_style="blue",
                box=box.ROUNDED,
                expand=False
            )

            table.add_column("Index", justify="center", style="yellow", width=10)
            table.add_column("Name", justify="left", style="white", width=25)
            table.add_column("Location", justify="left", style="cyan", width=20)
            table.add_column("Date", justify="center", style="green", width=25)
            table.add_column("Status", justify="center", style="magenta", width=15)

            for i, tournament in enumerate(tournaments, 1):
                dates = f"{tournament['beginning_date']} → {tournament['ending_date']}"
                table.add_row(
                    str(i),
                    tournament['name'],
                    tournament['location'],
                    dates,
                    tournament['status']
                )

            console.print(Align.center(table))
        else:
            console.print(Align.center("[bold yellow]No tournaments registered yet.[/bold yellow]"))

        console.print()

        menu_table = Table(
            show_header=False,
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        menu_table.add_column(justify="center", style="white", width=22)
        menu_table.add_column(justify="center", style="white", width=22)
        menu_table.add_column(justify="center", style="white", width=22)
        menu_table.add_column(justify="center", style="white", width=22)

        menu_table.add_row(
            "[cyan]1 ➤  [/cyan]Create tournament",
            "[cyan]2 ➤  [/cyan]Select tournament",
            "[cyan]3 ➤  [/cyan]Delete tournament",
            "[cyan]4 ➤  [/cyan]Go back"
        )

        console.print(Align.center(menu_table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        while choice not in ["1", "2", "3", "4"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()

        return choice

    def select_tournament_by_index(self, tournaments):
        console.print()

        terminal_width = console.width
        text = " Select tournament index (0 to cancel) ➤ "
        padding = (terminal_width - len(text) - 5) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        try:
            choice_int = int(choice)
            if choice_int == 0:
                return None
            if 1 <= choice_int <= len(tournaments):
                return tournaments[choice_int - 1]
            else:
                console.print(Align.center("[red]❌ Invalid index![/red]"))
                input("\n[Press Enter to continue...]")
                return None
        except ValueError:
            console.print(Align.center("[red]❌ Please enter a valid number![/red]"))
            input("\n[Press Enter to continue...]")
            return None

    def display_reports_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = "[bold magenta]📊  REPORTS  📊[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        input("\n[bold yellow]➤ Press ENTER to go back...[/bold yellow]")

    def exit_message(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 5)

        message = Panel(
            "[bold magenta]Thank you for using Chess Manager ! Goodbye ! 👋[/bold magenta]",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        console.print(Align.center(message))
        console.print()
