import os
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

console = Console()

def display_loading(message, duration=2):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        task = progress.add_task(message, total=None)
        time.sleep(duration)
        progress.update(task, description="Selesai!")

def display_cfonts_text(text, font_style="block", colors=["magenta", "cyan"]):
    try:
        display_loading("LOADING TO GENERATE")
        # Gunakan cfonts untuk membuat teks bergaya
        os.system(f"npx cfonts {text} --font {font_style} --colors {','.join(colors)} --align center")
    except Exception as e:
        console.print(f"[bold red]Terjadi kesalahan: {e}[/bold red]")

def main():
    os.system("clear")
    console.print(
        Panel(
            "[bold red]██████╗  ██╗ ███████╗  █████╗   █████╗   █████╗\n██╔══██╗ ██║ ╚══███╔╝ ██╔══██╗ ██╔══██╗ ██╔══██╗\n██║  ██║ ██║   ███╔╝  ╚██████║ ╚██████║ ╚██████║[/bold red]\n[bold white]██║  ██║ ██║  ███╔╝    ╚═══██║  ╚═══██║  ╚═══██║\n██████╔╝ ██║ ███████╗  █████╔╝  █████╔╝  █████╔╝\n╚═════╝  ╚═╝ ╚══════╝  ╚════╝   ╚════╝   ╚════╝[/bold white]\n"
            "[bold white]PEMBUAT : DIZFLYZE\nYOUTUBE : DIZFLYZE999\nVERSION : v2.8.1 Ultimated\n",
            title="[ SC GENERATE TAMPILAN ]",
            border_style="red"
        )
    )
    console.print(f"[bold yellow]╭────────────[ TEKS TO BOLD ]")
    text_input = console.input("[bold yellow]╰─> [ MASUKAN TEKS ] : [/bold yellow]")
    console.print(
        Panel(
            "[bold cyan][1] BLOK\n"
            "[2] SIMPEL\n"
            "[3] GRID\n"
            "[4] SHADE",
            title="[ MENU BENTUK GAYA ]",
            border_style="green"
        )
    )
    console.print(f"[bold yellow]╭────────────[ PILIH MODEL BENTUK ]")
    font_choice = console.input("[bold yellow]╰─> [ PILIH MODEL ] : [/bold yellow]")
    font_styles = {
        "1": "block",
        "2": "simple",
        "3": "grid",
        "4": "shade"
    }
    font_style = font_styles.get(font_choice, "block")

    console.print(
        Panel(
            "[1] UNGU & BIRU MUDA\n"
            "[2] MERAH & KUNING\n"
            "[3] BIRU & HIJAU",
            title="WARNA TEKS",
            border_style="green"
        )
    )
    console.print(f"[bold yellow]╭────────────[ TEKS TO COLOR ]")
    color_choice = console.input("[bold yellow]╰─> [ WARNA YANG DI SUKAI ] : [/bold yellow]")
    colors_map = {
        "1": ["magenta", "cyan"],
        "2": ["red", "yellow"],
        "3": ["blue", "green"]
    }
    colors = colors_map.get(color_choice, ["magenta", "cyan"])

    display_cfonts_text(text_input, font_style, colors)
    os.system("exit")

if __name__ == "__main__":
    main()