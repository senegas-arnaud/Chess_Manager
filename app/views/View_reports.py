from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import box
import os

console = Console()


class View_reports:

    def display_tournaments_list(self, tournaments):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = "[bold magenta]📊  TOURNAMENT REPORTS  📊[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        if not tournaments:
            console.print(Align.center("[yellow]No tournaments available.[/yellow]"))
            console.print()
            console.input("\n[bold yellow]➤ Press ENTER to go back...[/bold yellow]")
            return None

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("Index", justify="center", style="cyan", width=10)
        table.add_column("Name", justify="left", style="white", width=25)
        table.add_column("Date", justify="center", style="green", width=25)
        table.add_column("Location", justify="left", style="white", width=20)
        table.add_column("Status", justify="center", style="yellow", width=15)

        for i, tournament in enumerate(tournaments, 1):
            dates = f"{tournament['beginning_date']} → {tournament['ending_date']}"

            status = tournament.get('status', 'inscription')
            status_colors = {
                'registration': '[yellow]Registration[/yellow]',
                'in progress': '[green]In progress[/green]',
                'done': '[red]Done[/red]'
            }
            status_display = status_colors.get(status, status)

            table.add_row(
                str(i),
                tournament['name'],
                dates,
                tournament['location'],
                status_display
            )

        console.print(Align.center(table))
        console.print()

        terminal_width = console.width
        text = f" Select tournament index (1-{len(tournaments)}, 0 to cancel) ➤ "
        padding = (terminal_width - len(text) - 5) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
        choice = input()

        try:
            choice_int = int(choice)
            if choice_int == 0:
                return None
            return choice_int
        except ValueError:
            console.print(Align.center("[red]❌ Invalid input![/red]"))
            input("\n[Press Enter to continue...]")
            return None

    def display_tournament_report(self, tournament, all_players):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 2)

        title = f"[bold magenta]🏆  {tournament['name'].upper()}  🏆[/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        players_dict = {p['national_id']: p for p in all_players}

        round_history = tournament.get('round_history', [])

        if not round_history:
            console.print(Align.center("[yellow]No rounds played yet.[/yellow]"))
            console.print()
        else:
            for round_data in round_history:
                self.display_round_matches(round_data, players_dict)
                console.print()

        self.display_scores_table(tournament, players_dict)
        console.print()

        self.display_winner(tournament, players_dict)

        console.input("\n[bold yellow]➤ Press ENTER to go back...[/bold yellow]")

    def display_round_matches(self, round_data, players_dict):
        round_title = f"[bold cyan]═══ {round_data['name']} ═══[/bold cyan]"
        console.print(Align.center(round_title))
        console.print()

        matches_table = Table(
            show_header=False,
            border_style="blue",
            box=box.SIMPLE,
            expand=False
        )

        matches_table.add_column(justify="center", width=60)

        for match in round_data['matches']:
            player1_id = match[0][0]
            player1_score = match[0][1]
            player2_id = match[1][0]
            player2_score = match[1][1]

            player1 = players_dict.get(player1_id, {})
            player2 = players_dict.get(player2_id, {})

            player1_name = f"{player1.get('name', '?')} {player1.get('surname', '?')}"
            player2_name = f"{player2.get('name', '?')} {player2.get('surname', '?')}"

            if player1_score > player2_score:
                match_display = f"[green]{player1_name}[/green] vs [red]{player2_name}[/red]"
            elif player2_score > player1_score:
                match_display = f"[red]{player1_name}[/red] vs [green]{player2_name}[/green]"
            else:
                match_display = f"[blue]{player1_name}[/blue] vs [blue]{player2_name}[/blue]"

            matches_table.add_row(match_display)

        console.print(Align.center(matches_table))

    def display_scores_table(self, tournament, players_dict):
        console.print(Align.center("[bold cyan]═══ FINAL SCORES ═══[/bold cyan]"))
        console.print()

        player_scores = tournament.get('player_scores', {})

        if not player_scores:
            console.print(Align.center("[yellow]No scores available.[/yellow]"))
            return

        sorted_scores = sorted(
            player_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        scores_table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        scores_table.add_column("N°", justify="center", style="cyan", width=8)
        scores_table.add_column("Player", justify="left", style="white", width=35)
        scores_table.add_column("Score", justify="center", style="yellow", width=12)

        for rank, (player_id, score) in enumerate(sorted_scores, 1):
            player = players_dict.get(player_id, {})
            player_name = f"{player.get('name', '?')} {player.get('surname', '?')}"

            rank_display = str(rank)
            if rank == 1:
                rank_display = "🥇"
            elif rank == 2:
                rank_display = "🥈"
            elif rank == 3:
                rank_display = "🥉"

            scores_table.add_row(
                rank_display,
                player_name,
                f"{score} pts"
            )

        console.print(Align.center(scores_table))

    def display_winner(self, tournament, players_dict):
        winner = tournament.get('winner')

        if not winner:
            console.print(Align.center("[yellow]No winner determined yet.[/yellow]"))
            return

        console.print()

        if isinstance(winner, list):
            winner_names = []
            for w_id in winner:
                player = players_dict.get(w_id, {})
                winner_names.append(f"{player.get('name', '?')} {player.get('surname', '?')}")

            winner_text = Align.center(
                f"[bold yellow]🎊 TIE 🎊[/bold yellow]\n\n"
                f"[bold white]{' & '.join(winner_names)}[/bold white]"
            )
        else:
            player = players_dict.get(winner, {})
            winner_name = f"{player.get('name', '?')} {player.get('surname', '?')}"

            winner_text = (
                f"[bold yellow]👑 CHAMPION 👑[/bold yellow]\n\n"
                f"[bold white]{winner_name}[/bold white]"
            )

        winner_panel = Panel(
            Align.center(winner_text),
            title="[bold green]🏆 TOURNAMENT WINNER 🏆[/bold green]",
            border_style="bold green",
            box=box.DOUBLE,
            expand=False,
            padding=(1, 2)
        )

        console.print(Align.center(winner_panel))
