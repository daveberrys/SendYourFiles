from termcolor import colored
from datetime import datetime

# all of these are defined because I like doing `print.success("hi :3")`
# shut up
def success(m):
    s = "  SUCCESS  "
    c = "green"
    pta(s, c, m)
def error(m):
    s = "   ERROR   "
    c = "light_red"
    pta(s, c, m)
def fatal(m):
    s = "   FATAL   "
    c = "red"
    pta(s, c, m)
def debug(m):
    s = "   DEBUG   "
    c = "grey"
    pta(s, c, m)
def warning(m):
    s = "  WARNING  "
    c = "yellow"
    pta(s, c, m)

def pta(t, c, m):
    dt = datetime.now()
    fm = dt.strftime("%H:%M:%S")
    print(
        colored(f"( {fm} )", "dark_grey", force_color=True)
        + " - " +
        colored(f"[{t}]", c, force_color=True)
        + " " +
        m
    )