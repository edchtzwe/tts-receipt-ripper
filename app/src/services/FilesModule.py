import os;
from zoneinfo import ZoneInfo
from datetime import datetime
import re;
import shutil;
from pathlib import Path

class FilesModule:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent / "data"
    QUEUED_DIR = BASE_DIR / "queued"
    DOING_DIR = BASE_DIR / "doing"
    DONE_DIR = BASE_DIR / "done"
    LOCALTIMEZONE = None
    AUSTRALIA = "Australia/Melbourne"
    MALAYSIA = "Asia/Kuala_Lumpur"

    def __init__(self):
        # Ensure required directories exist
        os.makedirs(self.QUEUED_DIR, exist_ok=True)
        os.makedirs(self.DOING_DIR, exist_ok=True)
        os.makedirs(self.DONE_DIR, exist_ok=True)
        self.LOCALTIMEZONE = ZoneInfo(self.MALAYSIA)

    def print_directories(self):
        print("Directories:")
        print(f"QUEUED_DIR: {self.QUEUED_DIR}")
        print(f"DOING_DIR: {self.DOING_DIR}")
        print(f"DONE_DIR: {self.DONE_DIR}")

    def getSaveFileName(self, page_text, pageCount=""):
        receiptMatch = re.search(r"Voucher No\.: (\S+)", page_text)
        clientMatch = re.search(r"RECEIVED FROM: (.+)", page_text)

        receiptNumber = receiptMatch.group(1) if receiptMatch else "NoReceiptNumber"
        clientName = clientMatch.group(1).strip() if clientMatch else "NoClientName"

        nameString = f"{receiptNumber} {clientName}";
        if ((receiptNumber == "NoReceiptNumber" or clientName == "NoClientName") and len(pageCount)):
            nameString += f" at {pageCount}";


        return nameString;

    def getQueuedPath(self, fileName):
        return os.path.join(FilesModule.QUEUED_DIR, fileName)

    def getDoingPath(self, fileName):
        return os.path.join(FilesModule.DOING_DIR, fileName)

    def getOutputPdfPath(self, outputDir, saveFileName):
        return os.path.join(outputDir, f"{saveFileName}.pdf");

    def createOutputDir(self, outputDir):
        os.makedirs(outputDir, exist_ok=True)

    def getOutputDir(self):
        currentTime = datetime.now(self.LOCALTIMEZONE);
        formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")

        return os.path.join(FilesModule.DONE_DIR, formattedTime)

    def doQueue(self, queuedPath, doingPath):
        shutil.move(queuedPath, doingPath)
        print(f"Moved to doing: {doingPath}")

    def saveFilesToOutput(self, doingPath, outputDir):
        print("Moving files to Done.")
        shutil.move(doingPath, outputDir)
        print(f"Moved to done: {outputDir}")
