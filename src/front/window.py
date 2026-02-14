import webview as wv
import os
import sys

import src.back.util.print as print
from src.back.system.contact import API

def startUp(debugMode):
    def loadCSS(window):
        whereCss = os.path.join(os.path.dirname(__file__), "cacaStyle.css")
        with open(whereCss, "r") as f:
            css = f.read()
        window.load_css(css)

    here = os.path.join(os.path.dirname(__file__), "main", "index.html")
    print.debug(f"URL for HTTP is at {here}")

    if debugMode:
        print.success("Debug mode is enabled. I don't know why you'd want this.")

    # NO idea what this is, probably guessing PyInstaller's OneFile thingy.
    if getattr(sys, "frozen", False):
        projectRoot = sys._MEIPASS
    else:
        projectRoot = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

    iconExt = ".ico" if sys.platform == "win32" else ".png"
    iconPath = os.path.join(projectRoot, "assets", "icon", f"SendYourFiles{iconExt}")

    print.debug(f"Using icon at: {iconPath}")

    window = wv.create_window(
        title="Send Your Files",
        url=here,
        js_api=API(),

        width=800,
        height=600,
    )

    window.events.loaded += loadCSS
    wv.start(
        http_server=True,
        private_mode=True,

        debug=debugMode,
        icon=iconPath,
    )