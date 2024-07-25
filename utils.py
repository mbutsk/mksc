from typing import *


def shorten(number: float, rounding: int=2) -> str:
    '''
    Returns a shortened version of a number.
    '''
    decrease = 1000
    units = ["", " K", " M", " B", " T"]
    index = 0

    while (index != len(units)-1) and (number > decrease):
        number /= decrease
        index += 1

    return f'{round(number, rounding)}{units[index]}'


def shorten_dist(number: float) -> str:
    '''
    Returns a shortened version of a distance.
    '''
    decrease = 1000
    units = [" m", " km"]
    index = 0

    while (index != len(units)-1) and (number > decrease):
        number /= decrease
        index += 1

    return f'{number:.2f}{units[index]}'


def get_distance(p1: Tuple[float,float], p2: Tuple[float,float]) -> float:
    '''
    Returns distance between two 2D points.
    '''
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5


def lerp(a:float, b:float, t:float) -> float:
    '''
    Interpolates between A and B.
    '''
    t = max(0,min(1,t))
    return (1 - t) * a + t * b