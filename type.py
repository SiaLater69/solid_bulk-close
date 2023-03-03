from typing import Optional
import typer

app = typer.Typer()

@app.command()
def hello(name: Optional[str] = None):
    if name:
        typer.echo(f"Hello {name}")
    else:
        typer.echo("Hello World!")

# @app.command()
# def bye(name: Optional[str] = None):         
#     if name:
#         typer.echo(f"Bye {name}")
#     else:
#         typer.echo("Bye World!")

# @app.command()
# def age(age: Optional[int] = None):
#     if age:
#         typer.echo(f"Age {age}")
#     else:
#         typer.echo("You are a child bro sit down")
        

if __name__ == "__main__":
    app()

# def main():
#     typer.echo("Man Down")

if __name__ == "__main__":
    typer.run()