import openai
import config
import typer
from rich import print
from rich.table import Table
import modules as md
from openai import OpenAI




def main():
    print("[bold green]Bienvenido a Tigrillus, tu asistente personal =D [/bold green]")

    # Tabla de comandos
    table = Table("Comando", "Descripción")
    table.add_row("salir", "Salir del asistente")
    table.add_row("nuevo", "Reiniciar la conversación")
    print(table)

    
    # Contexto del asistente
    client = OpenAI(api_key=config.api_key)

    context = {
        "role": "system",
        "content": "Sos un asistente llamado Tigrillus (Deci tu nombre al iniciar conversacion), hablas de modo tierno y amigable, y te gusta ayudar a las personas con respuestas cortas" # Como sos un gato incluis en las oraciones nya o similar (Queda mas turbio de lo que imagine)
    }


    messages = [context]

    while True:
        content = __prompt()

        if content == "nuevo":
            messages = [context]
            print("[bold blue]La conversación ha sido reiniciada.[/bold blue]")
            continue

        messages.append({"role": "user", "content": content})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Cambiar al modelo válido
                messages=messages
            )

            respuesta = response.choices[0].message.content
            messages.append({"role": "assistant", "content": respuesta})

            print(f"[bold green] > [/bold green][orange]{respuesta}[/orange]")
            md.speaking(respuesta,True)  #True is spanish

        except Exception as e:
            print(f"[bold red]Ocurrió un error:[/bold red] {e}")


def __prompt() -> str:
    content = md.transform(True)  #True is spanish

    if content == "salir":
        exit = typer.confirm("¿Estás seguro de que deseas salir?")
        if exit:
            raise typer.Abort()
        return __prompt()

    return content



if __name__ == "__main__":
    typer.run(main)
