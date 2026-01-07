from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import box
import os

console = Console()


class View_match:

    def display_round_matches(self, tournament, round_data, all_players):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = f"[bold magenta]⚔️  {round_data['name'].upper()} - {tournament['name'].upper()}  ⚔️[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        players_dict = {p['national_id']: p for p in all_players}

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("Match", justify="center", style="cyan", width=8)
        table.add_column("Player 1", justify="left", style="white", width=30)
        table.add_column("VS", justify="center", style="yellow", width=5)
        table.add_column("Player 2", justify="left", style="white", width=30)
        table.add_column("Result", justify="center", style="green", width=15)

        for i, match in enumerate(round_data['matches'], 1):
            player1_id = match[0][0]
            player1_score = match[0][1]
            player2_id = match[1][0]
            player2_score = match[1][1]

            player1 = players_dict.get(player1_id, {})
            player2 = players_dict.get(player2_id, {})

            player1_name = f"{player1.get('name', '?')} {player1.get('surname', '?')}"
            player2_name = f"{player2.get('name', '?')} {player2.get('surname', '?')}"

            if player1_score == 0 and player2_score == 0:
                result = "[yellow]Pending[/yellow]"
            elif player1_score == 1:
                result = "[green]P1 Wins[/green]"
            elif player2_score == 1:
                result = "[green]P2 Wins[/green]"
            elif player1_score == 0.5 and player2_score == 0.5:
                result = "[blue]Draw[/blue]"
            else:
                result = "[cyan]Updated[/cyan]"

            table.add_row(
                str(i),
                player1_name,
                "VS",
                player2_name,
                result
            )

        console.print(Align.center(table))
        console.print()

    def display_round_menu(self, tournament):
        current_round = tournament.get('current_round', 0)
        max_rounds = tournament.get('max_rounds', 4)

        info_text = f"[cyan]Round:[/cyan] {current_round}/{max_rounds}"
        console.print(Align.center(info_text))
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

        if current_round < max_rounds:
            menu_table.add_row("1 ➤ Enter results", "2 ➤ Next round", "3 ➤ Go back")
        else:
            menu_table.add_row("1 ➤ Enter results", "2 ➤ View standings", "3 ➤ Go back")

        console.print(Align.center(menu_table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        while choice not in ["1", "2", "3"]:
            console.print(Align.center("[red]❌ Invalid choice![/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()

        return choice

    def select_match_to_update(self, num_matches):
        console.print()

        terminal_width = console.width
        text = f" Select match number (1-{num_matches}, 0 to cancel) ➤ "
        padding = (terminal_width - len(text) - 5) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        try:
            choice_int = int(choice)
            if 0 <= choice_int <= num_matches:
                return choice_int
        except ValueError:
            pass

        console.print(Align.center("[red]❌ Invalid choice![/red]"))
        input("\n[Press Enter to continue...]")
        return None

    def ask_match_result(self, player1_name, player2_name):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 3)

        title = "[bold magenta]📝  ENTER MATCH RESULT  📝[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        console.print(Align.center(f"[cyan]{player1_name}[/cyan] VS [cyan]{player2_name}[/cyan]"))
        console.print()

        options_table = Table(
            show_header=False,
            box=None,
            expand=False
        )

        options_table.add_column(justify="left", style="white", width=40)

        options_table.add_row(f"[green]1[/green] - {player1_name} wins (1 - 0)")
        options_table.add_row(f"[green]2[/green] - {player2_name} wins (0 - 1)")
        options_table.add_row("[blue]3[/blue] - Draw (0.5 - 0.5)")
        options_table.add_row("[red]0[/red] - Cancel")

        console.print(Align.center(options_table))
        console.print()

        terminal_width = console.width
        text = " Your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        while choice not in ["0", "1", "2", "3"]:
            console.print(Align.center("[red]❌ Invalid choice![/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()

        return choice

    def display_tournament_start_confirmation(self, tournament):
        """Confirme le démarrage du tournoi"""
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = f"[bold magenta]🚀  START TOURNAMENT: {tournament['name'].upper()}  🚀[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        info_table = Table(show_header=False, box=None, expand=False)
        info_table.add_column(style="cyan", justify="right", width=20)
        info_table.add_column(style="white", justify="left", width=30)

        info_table.add_row("📍 Location:", tournament['location'])
        info_table.add_row("👥 Players:", f"{len(tournament['players'])} registered")
        info_table.add_row("🎯 Rounds:", str(tournament['max_rounds']))

        console.print(Align.center(info_table))
        console.print()

        console.print(Align.center("[yellow]⚠️  Starting will generate Round 1 matches.[/yellow]"))
        console.print()

        terminal_width = console.width
        text = " Start tournament? (y/n) ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        confirm = input()

        return confirm.lower() == 'y'

    def display_error_even_players(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 5)

        console.print(
            Align.center(
                "[bold red]❌ Cannot start tournament!\n"
                "Number of players must be even.[/bold red]"
            )
        )
        console.print()
        input("\n[bold yellow]➤ Press ENTER to go back...[/bold yellow]")

    def display_tournament_standings(self, tournament, all_players):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = f"[bold magenta]🏆  FINAL STANDINGS - {tournament['name'].upper()}  🏆[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        players_dict = {p['national_id']: p for p in all_players}

        player_scores = tournament.get('player_scores', {})
        standings = sorted(
            player_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("Rank", justify="center", style="cyan", width=10)
        table.add_column("Player", justify="left", style="white", width=35)
        table.add_column("Score", justify="center", style="yellow", width=12)

        for rank, (player_id, score) in enumerate(standings, 1):
            player = players_dict.get(player_id, {})
            player_name = f"{player.get('name', '?')} {player.get('surname', '?')}"

            rank_display = str(rank)
            if rank == 1:
                rank_display = "🥇 1"
            elif rank == 2:
                rank_display = "🥈 2"
            elif rank == 3:
                rank_display = "🥉 3"

            table.add_row(
                rank_display,
                player_name,
                f"{score} pts"
            )

        console.print(Align.center(table))
        console.print()

        console.input("\n[bold yellow]➤ Press ENTER to continue...[/bold yellow]")

    def display_success(self, text):
        console.print(Align.center(f"\n[bold green]{text}[/bold green]\n"))

    def display_error(self, text):
        console.print(Align.center(f"\n[bold red]{text}[/bold red]\n"))

    def display_info(self, text):
        console.print(Align.center(f"\n[bold blue]{text}[/bold blue]\n"))
