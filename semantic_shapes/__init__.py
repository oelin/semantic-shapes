from dataclasses import dataclass
from typing import Optional


Unknown = None


@dataclass(frozen=True)
class ImageShape:
    channels: Optional[int] = Unknown
    height: Optional[int] = Unknown
    width: Optional[int] = Unknown


@dataclass(frozen=True)
class VolumeShape:
    channels: Optional[int] = Unknown
    width: Optional[int] = Unknown
    height: Optional[int] = Unknown
    depth: Optional[int] = Unknown 


@dataclass(frozen=True)
class VideoShape:
    duration: Optional[int] = Unknown
    channels: Optional[int] = Unknown
    height: Optional[int] = Unknown
    width: Optional[int] = Unknown


@dataclass(frozen=True)
class AudioShape:
    duration: Optional[int] = Unknown
    channels: Optional[int] = Unknown


@dataclass(frozen=True)
class TextShape:
    length: Optional[int] = Unknown


@dataclass(frozen=True)
class SequenceShape:
    channels: Optional[int] = Unknown
    length: Optional[int] = Unknown


# # Extras.

# def compose(x: dataclass, y: dataclass) -> dataclass:

#     fields = {**x.__dataclass_fields__, **y.__dataclass_fields__}
#     fields = [(field.name, field.type) for field in fields]
#     composite = dataclasses.make_dataclass('CompositeShape', fields)

#     return composite
