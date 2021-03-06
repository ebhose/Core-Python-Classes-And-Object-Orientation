#!/usr/bin/env python3


class Position:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValueError(f"Latitude {value} out of range")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValueError(f"Longitude {value} out of range")
        self._longitude = value

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.latitude >= 0 else "W"

    def __repr__(self):
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return (
            f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
            f"{abs(self.longitude)}° {self.longitude_hemisphere}"
        )

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}° {self.latitude_hemisphere}, "
            f"{longitude}° {self.longitude_hemisphere}"
        )


def typename(obj):
    return type(obj).__name__



class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass
