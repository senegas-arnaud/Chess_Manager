from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import box
import os

console = Console()


class View_tournament:

    def tournament_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 3)

        title = Panel(
            "[bold magenta]🏆  TOURNAMENT REGISTRATION  🏆[/bold magenta]",
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
        name = console.input("[bold yellow]📝 Enter tournament's name ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        location = console.input("[bold yellow]📝 Enter tournament's location ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        beginning_date = console.input(
            "[bold yellow]📅 Enter beginning date of tournament (YYYY-MM-DD) ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        ending_date = console.input("[bold yellow]📅 Enter ending date of tournament (YYYY-MM-DD) ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        remark = console.input("[bold yellow]📋 Add any additionnal remarks ➤[/bold yellow] ")
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))

        return name, location, beginning_date, ending_date, remark

    def display_error(self, text):
        console.print(Align.center(f"\n [bold red]{text}[/bold red] \n"))

    def display_success(self, text):
        console.print(Align.center(f"[bold green]{text}[/bold green] \n"))

    def display_info(self, text):
        console.print(Align.center(f"[bold blue]{text}[/bold blue] \n"))

    def display_and_select_tournaments(self, tournaments):
        os.system('cls' if os.name == 'nt' else 'clear')

        title = "[bold magenta]📋  SELECT A TOURNAMENT  📋[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("Index", justify="center", style="cyan", width=10)
        table.add_column("Name", justify="center", style="cyan", width=20)
        table.add_column("Location", justify="center", style="white", width=20)
        table.add_column("Beginning Date", justify="center", style="green", width=15)

        for i, tournament in enumerate(tournaments, 1):
            table.add_row(
                str(i),
                tournament["name"],
                tournament["location"],
                tournament["beginning_date"]
            )

        console.print(Align.center(table))
        console.print()

        choice = console.input("\n[bold yellow]Select tournament index (0 to cancel) ➤[/bold yellow]")

        try:
            choice_int = int(choice)
            if choice_int == 0:
                return None
            if 1 <= choice_int <= len(tournaments):
                return tournaments[choice_int - 1]
            else:
                console.print(Align.center("[red]❌ Invalid choice![/red]"))
                return None
        except ValueError:
            console.print(Align.center("[red]❌ Please enter a number![/red]"))
            return None

    def display_and_select_tournaments(self, tournaments):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = "[bold magenta]📋  SELECT A TOURNAMENT  📋[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("Index", justify="center", style="cyan", width=10)
        table.add_column("Name", justify="center", style="white", width=25)
        table.add_column("Location", justify="center", style="white", width=20)
        table.add_column("Beginning Date", justify="center", style="green", width=15)
        table.add_column("Players", justify="center", style="yellow", width=10)

        for i, tournament in enumerate(tournaments, 1):
            
            table.add_row(
                str(i),
                tournament["name"],
                tournament["location"],
                tournament["beginning_date"],
            )

        console.print(Align.center(table))
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
                console.print(Align.center("[red]❌ Invalid choice![/red]"))
                input("\n[Press Enter to continue...]")
                return None
        except ValueError:
            console.print(Align.center("[red]❌ Please enter a valid number![/red]"))
            input("\n[Press Enter to continue...]")
            return None

    def no_tournament(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 5)
        console.print(Align.center("[yellow]No tournaments registered yet.[/yellow]"))
        console.input("\n[bold yellow]➤ Press ENTER button to go back...[/bold yellow]")

    def display_tournament_management(self, tournament, all_players):
        """Affiche la page de gestion complète du tournoi"""
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = f"[bold magenta]⚙️  {tournament['name'].upper()}  ⚙️[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        info_text = (
            f"[cyan]📍 {tournament['location']}[/cyan]  |  "
            f"[green]📅 {tournament['beginning_date']} → {tournament['ending_date']}[/green]  |  "
        )
        console.print(Align.center(info_text))
        console.print()

        if tournament['players']:
            tournament_players = [
                p for p in all_players
                if p['national_id'] in tournament['players']
            ]

            table = Table(
                show_header=True,
                header_style="bold magenta",
                border_style="blue",
                box=box.ROUNDED,
                expand=False,
                title="[bold cyan]Registered Players[/bold cyan]"
            )

            table.add_column("N°", justify="center", style="cyan", width=5)
            table.add_column("Full Name", justify="left", style="white", width=30)
            table.add_column("National ID", justify="center", style="yellow", width=12)
            table.add_column("Birthday", justify="center", style="green", width=12)

            for i, player in enumerate(tournament_players, 1):
                full_name = f"{player['name']} {player['surname']}"
                table.add_row(
                    str(i),
                    full_name,
                    player['national_id'],
                    player['birthday']
                )

            console.print(Align.center(table))
        else:
            console.print(Align.center("[yellow]No players registered yet.[/yellow]"))

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

        menu_table.add_row("1 ➤ Add player", "2 ➤ Delete player", "3 ➤ Go back")

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

    def player_registration(self):
        """Demande l'ID du joueur à inscrire"""
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 3)

        title = Panel(
            "[bold magenta]👤  PLAYER REGISTRATION  👤[/bold magenta]",
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
        national_id = console.input(
            "[bold yellow]🆔 Enter player's national ID (0 to cancel) ➤[/bold yellow] "
        )
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))

        return national_id.strip().upper()

    def select_player_to_delete(self, tournament, all_players):
        """Sélectionner un joueur à supprimer"""
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = f"[bold red]🗑️  DELETE PLAYER FROM {tournament['name'].upper()}  🗑️[/bold red]"
        console.print(Align.center(Panel(title, style="bold red", expand=False)))
        console.print()

        if not tournament['players']:
            console.print(Align.center("[yellow]No players to delete.[/yellow]"))
            input("\n[Press Enter to continue...]")
            return None

        tournament_players = [
            p for p in all_players
            if p['national_id'] in tournament['players']
        ]

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="red",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("N°", justify="center", style="cyan", width=5)
        table.add_column("Full Name", justify="left", style="white", width=30)
        table.add_column("National ID", justify="center", style="yellow", width=12)

        for i, player in enumerate(tournament_players, 1):
            full_name = f"{player['name']} {player['surname']}"
            table.add_row(
                str(i),
                full_name,
                player['national_id']
            )

        console.print(Align.center(table))
        console.print()

        terminal_width = console.width
        text = " Select player number to delete (0 to cancel) ➤ "
        padding = (terminal_width - len(text) - 5) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        try:
            choice_int = int(choice)
            if choice_int == 0:
                return None
            if 1 <= choice_int <= len(tournament_players):
                return tournament_players[choice_int - 1]['national_id']
            else:
                console.print(Align.center("[red]❌ Invalid choice![/red]"))
                input("\n[Press Enter to continue...]")
                return None
        except ValueError:
            console.print(Align.center("[red]❌ Please enter a valid number![/red]"))
            input("\n[Press Enter to continue...]")
            return None