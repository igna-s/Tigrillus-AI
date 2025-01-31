import openai
import config
import typer
from rich import print
from rich.table import Table
import modules as md
from openai import OpenAI








def main():
    print("[bold green]Welcome to Tigrillus, your personal assistant =D [/bold green]")

    # Command table
    table = Table("Command", "Description")
    table.add_row("exit", "Exit the assistant")
    table.add_row("new", "Restart the conversation")
    print(table)

    
    # Assistant's context
    client = OpenAI(api_key=config.api_key)

    context = {
        "role": "system",
        "content": "You are an assistant named Tigrillus (Say your name at the beginning of the conversation), you speak in a cute and friendly manner, and you like to help people with short answers" # Since you are a cat, include 'nya' or similar in sentences (It sounds stranger than I imagined)
    }


    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            messages = [context]
            print("[bold blue]The conversation has been restarted.[/bold blue]")
            continue

        messages.append({"role": "user", "content": content})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Change to a valid model
                messages=messages
            )

            answer = response.choices[0].message.content
            messages.append({"role": "assistant", "content": answer})

            print(f"[bold green] > [/bold green][orange]{answer}[/orange]")
            md.speaking(answer, False)  # True is Spanish

        except Exception as e:
            print(f"[bold red]An error occurred:[/bold red] {e}")


def __prompt() -> str:
    content = md.transform(False)  # True is Spanish

    if content == "exit":
        exit = typer.confirm("Are you sure you want to exit?")
        if exit:
            raise typer.Abort()
        return __prompt()

    return content


if __name__ == "__main__":
    typer.run(main)
