import webview
import os
import sys

from src.back.api.sendingFile import catbox, litterbox, buzzheavier
from src.back.api.checkForUpdate import isUpdateAvailable
from src.back.util.notify import notify
import src.back.util.print as print

class API:
    def pickFile(self):
        window = webview.active_window()
        file_path = window.create_file_dialog(webview.FileDialog.OPEN)
        if file_path:
            path = file_path[0]
            size = os.path.getsize(path)
            return {"path": path, "size": size}
        return None

    def uploadTo(self, path, platform, duration="1h"):
        filename = os.path.basename(path)
        notify("Upload Started", f"Sending {filename} to {platform}...")

        result = ""
        if platform == "catbox":
            result = catbox(path)
        elif platform == "litterbox":
            result = litterbox(path, duration)
        elif platform == "buzzheavier":
            result = buzzheavier(path)
        else:
            result = "Unknown platform"

        if result.startswith("http"):
            notify("Upload Success!", f"Link: {result}")
        else:
            notify("Upload Failed", f"Problem with {platform}: {result}")

        return result

    def checkForUpdates(self):
        # checks if the local file exists
        try:
            if getattr(sys, 'frozen', False):
                basePath = sys._MEIPASS
            else:
                basePath = os.path.abspath(".")
            
            versionPath = os.path.join(basePath, "version.txt")
            with open(versionPath, "r") as f:
                currentVersion = f.read().strip()
            print.success(f"Local file found! Current version: {currentVersion}")
        except Exception as e:
            print.error(f"Local file error: {e}")
            return {"status": "error", "message": f"Local file error: {e}"}

        # contacts github for the latest update
        try:
            print.debug("Checking for updates...")
            return isUpdateAvailable(currentVersion)
        except Exception as e:
            print.error(f"Network error: {e}")
            return {"status": "error", "message": f"Network error: {e}"}