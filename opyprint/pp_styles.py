from __future__ import annotations

from enum import Enum, unique


@unique
class PPStyles(str, Enum):
    # styles:
    blink = "blink"
    blink_end = "blink_end"
    bold = "bold"
    default = "default"
    dim = "dim"
    inverse = "inverse"
    inverse_end = "inverse_end"
    invert = "invert"
    invert_end = "invert_end"
    italic = "italic"
    normal = "normal"
    reset = "reset"
    strike = "strike"
    strike_end = "strike_end"
    underline = "underline"

    # text/fg colors:
    black = "black"
    blue = "blue"
    blue_d1 = "blue_d1"
    blue_d2 = "blue_d2"
    blue_l1 = "blue_l1"
    cyan = "cyan"
    cyan_d1 = "cyan_d1"
    cyan_d2 = "cyan_d2"
    cyan_l1 = "cyan_l1"
    green = "green"
    green_d1 = "green_d1"
    green_d2 = "green_d2"
    green_l1 = "green_l1"
    magenta = "magenta"
    magenta_d1 = "magenta_d1"
    magenta_d2 = "magenta_d2"
    magenta_l1 = "magenta_l1"
    pink = "pink"
    pink_d1 = "pink_d1"
    pink_d2 = "pink_d2"
    pink_l1 = "pink_l1"
    orange = "orange"
    orange_d1 = "orange_d1"
    orange_d2 = "orange_d2"
    orange_l1 = "orange_l1"
    red = "red"
    red_d1 = "red_d1"
    red_d2 = "red_d2"
    red_l1 = "red_l1"
    white = "white"
    yellow = "yellow"
    yellow_d1 = "yellow_d1"
    yellow_d2 = "yellow_d2"
    yellow_l1 = "yellow_l1"

    # bold text/fg colors:
    b_black = "b_black"
    b_blue = "b_blue"
    b_blue_d1 = "b_blue_d1"
    b_blue_d2 = "b_blue_d2"
    b_blue_l1 = "b_blue_l1"
    b_cyan = "b_cyan"
    b_cyan_d1 = "b_cyan_d1"
    b_cyan_d2 = "b_cyan_d2"
    b_cyan_l1 = "b_cyan_l1"
    b_green = "b_green"
    b_green_d1 = "b_green_d1"
    b_green_d2 = "b_green_d2"
    b_green_l1 = "b_green_l1"
    b_magenta = "b_magenta"
    b_magenta_d1 = "b_magenta_d1"
    b_magenta_d2 = "b_magenta_d2"
    b_magenta_l1 = "b_magenta_l1"
    b_pink = "b_pink"
    b_pink_d1 = "b_pink_d1"
    b_pink_d2 = "b_pink_d2"
    b_pink_l1 = "b_pink_l1"
    b_orange = "b_orange"
    b_orange_d1 = "b_orange_d1"
    b_orange_d2 = "b_orange_d2"
    b_orange_l1 = "b_orange_l1"
    b_red = "b_red"
    b_red_d1 = "b_red_d1"
    b_red_d2 = "b_red_d2"
    b_red_l1 = "b_red_l1"
    b_white = "b_white"
    b_yellow = "b_yellow"
    b_yellow_d1 = "b_yellow_d1"
    b_yellow_d2 = "b_yellow_d2"
    b_yellow_l1 = "b_yellow_l1"

    # background colors:
    bg_black = "bg_black"
    bg_blue = "bg_blue"
    bg_cyan = "bg_cyan"
    bg_green = "bg_green"
    bg_grey = "bg_grey"
    bg_magenta = "bg_magenta"
    bg_orange = "bg_orange"
    bg_red = "bg_red"
    bg_white = "bg_white"
    bg_yellow = "bg_yellow"

    # darker variations of background colors:
    bg_blue_d1 = "bg_blue_d1"
    bg_blue_d2 = "bg_blue_d2"
    bg_blue_d3 = "bg_blue_d3"
    bg_cyan_d1 = "bg_cyan_d1"
    bg_cyan_d2 = "bg_cyan_d2"
    bg_green_d1 = "bg_green_d1"
    bg_green_d2 = "bg_green_d2"
    bg_grey_d1 = "bg_grey_d1"
    bg_grey_d2 = "bg_grey_d2"
    bg_grey_d3 = "bg_grey_d3"
    bg_grey_d4 = "bg_grey_d4"
    bg_magenta_d1 = "bg_magenta_d1"
    bg_magenta_d2 = "bg_magenta_d2"
    bg_magenta_d3 = "bg_magenta_d3"
    bg_red_d1 = "bg_red_d1"
    bg_red_d2 = "bg_red_d2"
    bg_red_d3 = "bg_red_d3"
    bg_orange_d1 = "bg_orange_d1"
    bg_orange_d2 = "bg_orange_d2"
    bg_orange_d3 = "bg_orange_d3"
    bg_yellow_d1 = "bg_yellow_d1"
    bg_yellow_d2 = "bg_yellow_d2"

    # background colors with bold foreground:
    bg_b_black = "bg_b_black"
    bg_b_blue = "bg_b_blue"
    bg_b_cyan = "bg_b_cyan"
    bg_b_green = "bg_b_green"
    bg_b_grey = "bg_b_grey"
    bg_b_magenta = "bg_b_magenta"
    bg_b_orange = "bg_b_orange"
    bg_b_red = "bg_b_red"
    bg_b_white = "bg_b_white"
    bg_b_yellow = "bg_b_yellow"

    # extended colors:
    grey = "grey"
    grey_0 = "grey_0"
    grey_1 = "grey_1"
    grey_2 = "grey_2"
    grey_3 = "grey_3"
    grey_4 = "grey_4"
    grey_5 = "grey_5"

    # bold extended colors:
    b_grey = "b_grey"
    b_grey_0 = "b_grey_0"
    b_grey_1 = "b_grey_1"
    b_grey_2 = "b_grey_2"
    b_grey_3 = "b_grey_3"
    b_grey_4 = "b_grey_4"
    b_grey_5 = "b_grey_5"
