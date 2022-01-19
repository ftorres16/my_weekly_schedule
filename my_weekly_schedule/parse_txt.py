from pathlib import Path

from pydantic import ValidationError

from my_weekly_schedule.models import Event


def parse_txt(in_path: Path) -> list[Event]:

    with open(in_path) as f:
        lines = f.readlines()

    events = []

    for line0, line1, line2, line3 in zip(lines, lines[1:], lines[2:], lines[3:]):
        try:
            event = Event(title=line0, day=line1, start=line2, end=line2, color=line3)
            events.append(event)
        except ValidationError:
            continue

    return events
