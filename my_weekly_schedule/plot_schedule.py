import datetime
import typing as T
from math import ceil
from pathlib import Path

import matplotlib.pyplot as plt

from my_weekly_schedule.models import Event, WeekdayEnum


def plot_events(
    events: list[Event],
    show: bool,
    with_weekends: bool,
    save_img: bool,
    out_path: T.Optional[Path] = None,
):
    """
    Generate the schedule as a matplotlib plot.
    """
    if save_img and out_path is None:
        raise ValueError("Attempted to save image, but no output path was given.")

    fig = plt.figure(figsize=(18, 9))

    for event in events:
        min_x = event.day.value + 0.5
        max_x = min_x + 0.96

        min_y = time_to_hours(event.start)
        max_y = time_to_hours(event.end)

        plt.fill_between(
            [min_x, max_x], [min_y, min_y], [max_y, max_y], color=event.color.as_named()
        )
        plt.text(
            min_x + 0.02,
            min_y + 0.02,
            event.start.strftime("%H:%M"),
            va="top",
            fontsize=8,
        )

        plt.text(
            (min_x + max_x) / 2,
            (min_y + max_y) / 2,
            event.title,
            ha="center",
            va="center",
            fontsize=10,
        )

    plt.title("Weekly Schedule", y=1, fontsize=14)

    [ax] = fig.axes

    days = [day.name.title() for day in WeekdayEnum if with_weekends or day.value < 5]

    ax.set_xlim(0.5, len(days) + 0.5)
    ax.set_xticks(range(1, len(days) + 1))
    ax.set_xticklabels(days)

    earliest = min(time_to_hours(event.start) for event in events)
    latest = max(time_to_hours(event.end) for event in events)

    earliest = ceil(earliest)
    latest = ceil(latest)

    ax.set_ylim(latest, earliest)
    ax.set_yticks(range(earliest, latest))
    ax.set_yticklabels([f"{h}:00" for h in range(earliest, latest)])

    ax.grid(axis="y", linestyle="--", linewidth=0.5)

    if save_img:
        plt.savefig(
            out_path,
            dpi=200,
            bbox_inches="tight",
        )

    if show:
        plt.show()


def time_to_hours(time: datetime.time) -> float:
    return time.hour + time.minute / 60
