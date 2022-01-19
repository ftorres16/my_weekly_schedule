from pathlib import Path

import matplotlib.pyplot as plt
import typer

from my_weekly_schedule.parse_txt import parse_txt
from my_weekly_schedule.plot_schedule import plot_events

app = typer.Typer()


def main(
    input_: Path,
    show: bool = True,
    save_img: bool = True,
    with_weekends: bool = False,
):
    """
    Plot weekly schedule schedule.
    """
    events = parse_txt(input_)

    out_path = input_.with_suffix(".png")

    plot_events(
        events,
        with_weekends=with_weekends,
        show=show,
        save_img=save_img,
        out_path=out_path,
    )


if __name__ == "__main__":
    typer.run(main)
