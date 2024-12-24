import os
import random
from PIL import Image
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from argparse import ArgumentParser
import shutil

console = Console()

# warna teks
def color_text(text, color):
    return f"[{color}]{text}[/{color}]"

# file/folder
os.system("clear")
def get_image_from_path(path):
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        task = progress.add_task("LOADING TO OPEN SCRIPT", total=None)
        if os.path.isfile(path):
            progress.update(task, description="File ready bosku")
            return path
        elif os.path.isdir(path):
            images = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            if images:
                progress.update(task, description="Mencoba mengubah")
                return os.path.join(path, random.choice(images))
            else:
                console.print(color_text("Gambar tidak ada", "yellow"))
                return None
        else:
            console.print(color_text("Tempatnya beda mungkin", "red"))
            return None

# program
def image_to_ascii(image_path, new_width=99999999999, colored=False):
    try:
        # konver
        img = Image.open(image_path).convert("L")
        aspect_ratio = img.height / img.width
        new_height = int(aspect_ratio * new_width * 0.50)  # Rasio lebih akurat untuk terminal
        img = img.resize((new_width, new_height))

        # kode
        ascii_chars = " .,:;#"
        pixels = img.getdata()

        # detail
        ascii_str = ""
        with Progress(
            SpinnerColumn(), BarColumn(), TextColumn("[progress.description]{task.description}"), transient=True
        ) as progress:
            task = progress.add_task("Mengonversi ke ASCII...", total=len(pixels))
            for pixel in pixels:
                ascii_str += ascii_chars[int(pixel / 500 * (len(ascii_chars) - 1))]
                progress.update(task, advance=1)

       
        ascii_str = "\n".join([ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)])
        
        # support warna
        if colored:
            ascii_str = "\n".join(
                [color_text(line, "cyan") for line in ascii_str.split("\n")]
            )
        
        return ascii_str
    except Exception as e:
        console.print(color_text(f"Kesalahan saat memproses gambar: {e}", "red"))
        return None

# hasil
os.system("clear")
def display_result(ascii_art, save_path=None):
    if save_path:
        with open(save_path, "w") as f:
            f.write(ascii_art)
        console.print(
            Panel(
                f"999 DIZ FLYZE 999 SV DATA KE : {save_path}",
                border_style="green",
                title="Sukses",
            )
        )
    else:
        console.print(Panel(ascii_art, title="[ 999 DIZ FLYZE 999 ]", border_style="cyan"))

# Home
os.system("clear")
def main():
    # Header
    console.print(Panel("[bold cyan]SCRIPT CREATE TEKS GAMBAR[/bold cyan]\n[italic green]DIZ FLYZE DEVELOPER SCRIPT TEKS TO IMAGE[/italic green]", title="[ DIZ FLYZE ]", border_style="blue"))

    # pararg
    parser = ArgumentParser(description="DIZ FLYZE DEVELOPER SCRIPT")
    parser.add_argument("path", type=str, nargs="?", default=".", help="Path ke file atau folder gambar (default: current directory).")
    parser.add_argument("--width", type=int, default=40, help="LEBAR LAYAR")
    parser.add_argument("--save", type=str, help="SV KE INTERNAL")
    parser.add_argument("--colored", action="store_true", help="TEKS WARNA")
    args = parser.parse_args()

    # file/forlder validasi
    image_path = get_image_from_path(args.path)
    if image_path:
        console.print(color_text(f"BERHASIL MEMBUAT", "green"))
        ascii_art = image_to_ascii(image_path, new_width=args.width, colored=args.colored)
        if ascii_art:
            display_result(ascii_art, save_path=args.save)
        else:
            console.print(color_text("GAGAL", "yellow"))
    else:
        console.print(color_text("GAMBAR TIDAK BISA DI UBAH", "red"))

if __name__ == "__main__":
    main()