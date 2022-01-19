import typer

from my_weekly_schedule.parse_txt import parse_txt

app = typer.Typer()


def main(input_: typer.FileText):
    """
    Plot weekly schedule schedule.
    """
    events = parse_txt(input_.readlines())

    typer.echo(events)

    import ipdb

    ipdb.set_trace()


if __name__ == "__main__":
    typer.run(main)
