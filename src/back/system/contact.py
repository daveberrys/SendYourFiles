import webview
import os

from src.back.api.sendingFile import catbox, litterbox, buzzheavier
from src.back.api.checkForUpdate import isUpdateAvailable

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
        if platform == "catbox":
            return catbox(path)
        elif platform == "litterbox":
            return litterbox(path, duration)
        elif platform == "buzzheavier":
            return buzzheavier(path)
        return "Unknown platform"

    def checkForUpdates(self):
        try:
            with open("version.txt", "r") as f:
                currentVersion = f.read().strip()
            return isUpdateAvailable(currentVersion)
        except Exception as e:
            return f"Error: {str(e)}"