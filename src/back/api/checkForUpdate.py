import requests
import src.back.util.print as print

urlToVersion = "https://raw.githubusercontent.com/daveberrys/SendYourFIles/refs/heads/main/version.txt"

def getLatestVersion():
    try:
        response = requests.get(urlToVersion, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        return None
    except Exception as e:
        print.error(f"Update check failed: {e}")
        return None

def isUpdateAvailable(currentVersion):
    latest = getLatestVersion()
    
    if latest is None:
        return {"status": "error"}

    print.debug(f"Latest version is {latest} and current version is {currentVersion}")
    if latest != currentVersion:
        print.debug(f"Update available! {latest} is newer than {currentVersion}")
        return {"status": "success", "available": True, "latest": latest}
    
    print.debug(f"No update available. {latest} is the latest version.")
    return {"status": "success", "available": False, "latest": currentVersion}