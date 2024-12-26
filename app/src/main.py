from services.PdfModule import PdfModule;
from services.FilesModule import FilesModule;
import os;
import time;
import shutil;

class Main:
    filesModule = None;
    pdfModule = None;

    def __init__(self):
        self.filesModule = FilesModule();
        self.pdfModule = PdfModule();

    def processFiles(self, queuedFiles):
        if (not len(queuedFiles)):
            print("No files in queue... Standing by...");
            time.sleep(3);

            return False;

        for fileName in queuedFiles:
            queuedPath = self.filesModule.getQueuedPath(fileName)
            doingPath = self.filesModule.getDoingPath(fileName)

            self.filesModule.doQueue(queuedPath, doingPath)

            outputDir = self.filesModule.getOutputDir();

            result = self.pdfModule.splitPdf(doingPath, outputDir);
            if (not result):
                print("The process failed.");
                print("Move the PDF back into the queue to try again...");
                print("Entering stand by mode...");

                pass;

            print(f"Successfully processed {result} files");
            self.filesModule.saveFilesToOutput(doingPath, outputDir);

        print("The queue is now clear... Standing by...");
        time.sleep(3);

    def execute(self):
        print("The receipt ripper is ready. Press Ctrl + C to terminate...");

        while True:
            self.processFiles(os.listdir(FilesModule.QUEUED_DIR));

app = Main();
app.execute();
