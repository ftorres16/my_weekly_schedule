from pathlib import Path

import typer

from my_weekly_schedule.models import WeekdayEnum
from my_weekly_schedule.parse_txt import parse_txt
from my_weekly_schedule.plot_schedule import plot_events

app = typer.Typer()


@app.command()
def main(
    input_: Path,
    show: bool = True,
    save_img: bool = True,
    weekends: bool = True,
):
    """
    Plot weekly schedule schedule.
    """
    events = parse_txt(input_)

    if not weekends and any(
        event.day.value > WeekdayEnum.fri.value for event in events
    ):
        typer.echo("Attempted to plot without weekends, but there are weekend events.")
        raise typer.Abort()

    out_path = input_.with_suffix(".png")

    plot_events(
        events,
        with_weekends=weekends,
        show=show,
        save_img=save_img,
        out_path=out_path,
    )


if __name__ == "__main__":
    app()
