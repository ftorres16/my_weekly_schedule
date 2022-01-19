from datetime import time
from enum import Enum

from pydantic import BaseModel, constr, validator
from pydantic.color import Color


class WeekdayEnum(Enum):
    mon = 0
    tue = 1
    wed = 2
    thu = 3
    fri = 4
    sat = 5
    sun = 6


class Event(BaseModel):
    title: constr(min_length=1, strip_whitespace=True)
    day: WeekdayEnum
    start: time
    end: time
    color: Color

    @validator("day", pre=True)
    def get_enum_from_str(cls, v):
        if isinstance(v, str):
            try:
                return WeekdayEnum[v.strip().lower()]
            except KeyError:
                raise ValueError(
                    "Day must be one of: Mon, Tue, Wed, Thu, Fri, Sat, Sun"
                )
        return v

    @validator("start", pre=True)
    def get_start_time(cls, v):
        if isinstance(v, str) and len(v.split("-")) == 2:
            return v.split("-")[0].strip()
        return v

    @validator("end", pre=True)
    def get_end_time(cls, v):
        if isinstance(v, str) and len(v.split("-")) == 2:
            return v.split("-")[1].strip()
        return v

    @validator("end")
    def ends_after_start(cls, v, values, **kwargs):
        if "start" in values and values["start"] >= v:
            raise ValueError("Event must end after it starts")
        return v

    @validator("color", pre=True)
    def strip_whitespace(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v
