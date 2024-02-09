import requests

from enum import Enum
from pydantic import BaseModel, field_validator, Field
from typing import Callable, Generator, Self, Optional, List



class Part(Enum):
    night = "Ночь"
    morning  = "Утро"
    day = "День"
    evening  = "Вечер"

class Wind(Enum):
    nw = "северо-западное"
    n = "северное"
    ne = "северо-восточное"
    e = "восточное"
    se = "юго-восточное"
    s = "южное"
    sw = "юго-западное"
    w = "западное"
    c = "штиль"

class Condition(Enum):
    clear = "ясно"
    partly_cloudy = "малооблачно"
    cloudy = "облачно с прояснениями"
    overcast = "пасмурно"
    light_rain = "небольшой дождь"
    rain = "дождь"
    heavy_rain = "сильный дождь"
    showers = "ливень"
    wet_snow = "дождь со снегом"
    light_snow = "небольшой снег"
    snow = "снег"
    snow_showers = "снегопад"
    hail = "град"
    thunderstorm = "гроза"
    thunderstorm_with_rain = "дождь с грозой"
    thunderstorm_with_hail = "гроза с градом"

moon_code: dict = {
    "moon-code-0": "полнолуние",
    "moon-code-1": "убывающая луна",
    "moon-code-2": "убывающая луна",
    "moon-code-3": "убывающая луна",
    "moon-code-4": "последняя четверть",
    "moon-code-5": "убывающая луна",
    "moon-code-6": "убывающая луна",
    "moon-code-7": "убывающая луна",
    "moon-code-8": "новолуние",
    "moon-code-9": "растущая луна",
    "moon-code-10": "растущая луна",
    "moon-code-11": "растущая луна",
    "moon-code-12": "первая четверть",
    "moon-code-13": "растущая луна",
    "moon-code-14": "растущая луна",
    "moon-code-15": "растущая луна"
}


class Basic_Weather(BaseModel):
    temp: int
    feels_like: int
    condition: Condition
    wind_speed: float
    wind_dir: Wind

    @field_validator("wind_dir", mode="before")
    @classmethod
    def wind_validator(cls, wind_dir: str) -> Optional[Wind]:
        for val in Wind:
            if val.name == wind_dir:
                return val
        return None

    @field_validator("condition", mode="before")
    @classmethod
    def condition_validator(cls, title_w: str) -> Optional[Condition]:
        condition = title_w.replace('-', '_')
        for val in Condition:
            if val.name == condition:
                return val
        return None


class Extended_Weather_Info(BaseModel):
    part_name: str
    temp_max: int
    feels_like: int
    condition: Condition
    wind_speed: float
    humidity: int

    @field_validator("part_name")
    @classmethod
    def part_name_validator(cls, part_name: str) -> Optional[Part]:
        for part in Part:
            if part.name == part_name:
                return part
        return None

    @field_validator("condition", mode="before")
    @classmethod
    def condition_validator(cls, title_w: str) -> Optional[Condition]:
        condition = title_w.replace('-', '_')
        for val in Condition:
            if val.name == condition:
                return val
        return None


class Extended_Weather(BaseModel):
    sunset: str
    moon: str = Field(alias="moon_text")
    parts: List[Extended_Weather_Info]

    @field_validator("moon")
    @classmethod
    def moon_validator(cls, moon_c: str) -> Optional[str]:
        if moon_c in moon_code:
            return moon_code[moon_c]
        return None

class Weather(BaseModel):
    basic_info: Basic_Weather = Field(alias="fact")
    extended_info: Extended_Weather = Field(alias="forecast")