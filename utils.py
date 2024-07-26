from typing import *
from config import *


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


def get_heatmap_color(percent:float) -> str:
    '''
    Returns a hex color of a heatmap gradient at a certain pos.
    '''
    offset = len(HEATMAP_COLORS)-1
    opercent = percent*offset
    offset = min(offset-1,int(opercent))
    rpercent = opercent%1.0
    
    r = int(lerp(HEATMAP_COLORS[0+offset][0], HEATMAP_COLORS[1+offset][0], rpercent))
    g = int(lerp(HEATMAP_COLORS[0+offset][1], HEATMAP_COLORS[1+offset][1], rpercent))
    b = int(lerp(HEATMAP_COLORS[0+offset][2], HEATMAP_COLORS[1+offset][2], rpercent))

    return '#%02x%02x%02x' % (r,g,b)