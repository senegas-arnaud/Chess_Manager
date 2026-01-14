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
        name = console.input("[bold yellow]📝 Enter player's name (0 to cancel) ➤[/bold yellow] ")

        if name.strip() == "0":
            return None
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

    def display_secondary_menu(self):
        console.print()

        table = Table(
            show_header=False,
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column(justify="center", style="white", width=25)
        table.add_column(justify="center", style="white", width=25)

        table.add_row("[bold cyan]1 ➤   [/bold cyan]Add an other one", "[bold cyan]2 ➤   [/bold cyan]Go back")

        console.print(Align.center(table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        while choice not in ["1", "2"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()

        return choice

    def display_all_players(self, players):
        os.system('cls' if os.name == 'nt' else 'clear')

        if not players:
            console.print(Align.center("[yellow]No players registered yet.[/yellow]"))
            console.input("\n[bold yellow]➤ Press Enter to continue...[/bold yellow]")
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

        console.input("\n[bold yellow]➤  Press ENTER button to going back...[/bold yellow]")

    def ask_player_id_to_modify(self, players):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = Panel(
            "[bold magenta]✏️   MODIFY PLAYER  ✏️[/bold magenta]",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        console.print(Align.center(title))
        console.print()

        if players:

            table = Table(
                show_header=True,
                header_style="bold magenta",
                border_style="blue",
                box=box.ROUNDED,
                expand=False
            )

            table.add_column("Name", justify="left", style="white", width=20)
            table.add_column("National ID", justify="left", style="white", width=20)

            for i, player in enumerate(players, 1):
                full_name = f"{player['name']} {player['surname']}"

                table.add_row(
                    full_name,
                    player['national_id']
                )

            console.print(Align.center(table))
            console.print()
        else:
            console.print(Align.center("[yellow]No players registered yet.[/yellow]"))
            console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))
        console.print()

        terminal_width = console.width
        form_width = 50
        padding_left = (terminal_width - form_width) // 2

        console.print(" " * padding_left, end="")
        national_id = console.input(
            "[bold yellow]🆔 Enter player's national ID to modify (0 to cancel) ➤[/bold yellow] "
        )
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))

        return national_id.strip().upper()

    def display_player_current_info(self, player):
        console.print()
        console.print(Align.center("[bold cyan]Current information:[/bold cyan]"))
        console.print()

        info_table = Table(show_header=False, box=None, expand=False)
        info_table.add_column(style="cyan", justify="right", width=20)
        info_table.add_column(style="white", justify="left", width=30)

        info_table.add_row("Name:", player['name'])
        info_table.add_row("Surname:", player['surname'])
        info_table.add_row("Birthday:", player['birthday'])
        info_table.add_row("National ID:", player['national_id'])

        console.print(Align.center(info_table))
        console.print()
        console.print(Align.center("[yellow]Enter new information (leave blank to keep current)[/yellow]"))
        console.print()

    def player_modification_form(self, current_player):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 3)

        title = Panel(
            "[bold magenta]✏️  UPDATE PLAYER INFORMATION  ✏️[/bold magenta]",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        console.print(Align.center(title))
        console.print()

        self.display_player_current_info(current_player)

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))
        console.print()

        terminal_width = console.width
        form_width = 50
        padding_left = (terminal_width - form_width) // 2

        console.print(" " * padding_left, end="")
        name = console.input(
            f"[bold yellow]📝 New name [{current_player['name']}] ➤[/bold yellow] "
        )
        name = name.strip() if name.strip() else current_player['name']
        console.print()

        console.print(" " * padding_left, end="")
        surname = console.input(
            f"[bold yellow]📝 New surname [{current_player['surname']}] ➤[/bold yellow] "
        )
        surname = surname.strip() if surname.strip() else current_player['surname']
        console.print()

        console.print(" " * padding_left, end="")
        birthday = console.input(
            f"[bold yellow]📅 New birthday [{current_player['birthday']}] ➤[/bold yellow] "
        )
        birthday = birthday.strip() if birthday.strip() else current_player['birthday']
        console.print()

        console.print(" " * padding_left, end="")
        national_id = console.input(
            f"[bold yellow]🆔 New national ID [{current_player['national_id']}] ➤[/bold yellow] "
        )
        national_id = national_id.strip().upper() if national_id.strip() else current_player['national_id']
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))

        return name, surname, birthday, national_id
