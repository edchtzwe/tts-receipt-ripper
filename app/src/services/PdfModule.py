from PyPDF2 import PdfReader, PdfWriter
import os
import shutil
import re
from datetime import datetime
from services.FilesModule import FilesModule

class PdfModule:
    def getSaveFileName(self, page_text, pageCount=""):
        receiptMatch = re.search(r"Voucher No\.: (\S+)", page_text)
        clientMatch = re.search(r"RECEIVED FROM: (.+)", page_text)

        receiptNumber = receiptMatch.group(1) if receiptMatch else "NoReceiptNumber"
        clientName = clientMatch.group(1).strip() if clientMatch else "NoClientName"

        nameString = f"{receiptNumber} {clientName}";
        if ((receiptNumber == "NoReceiptNumber" or clientName == "NoClientName") and len(pageCount)):
            nameString += f" at {pageCount}";


        return nameString;

    def splitPdf(self, file_path, output_dir):
        if (not len(file_path)):
            return 0;

        reader = PdfReader(file_path)
        if (not len(reader.pages)):
            return 0;

        os.makedirs(output_dir, exist_ok=True)

        result = 0;
        for i, page in enumerate(reader.pages):
            pageText = page.extract_text()
            if (not len(pageText)):
                pass

            pageCount = f"page_{i+1}";
            saveFileName = self.getSaveFileName(pageText, pageCount);

            writer = PdfWriter()
            writer.add_page(page)
            output_pdf_path = os.path.join(output_dir, f"{saveFileName}.pdf")
            with open(output_pdf_path, "wb") as output_file:
                writer.write(output_file)
                print(f"Saved: {output_pdf_path}")
                result += 1;

        return result;

    def processFiles(self):
        queued_files = os.listdir(FilesModule.QUEUED_DIR)
        
        for fileName in queued_files:
            queued_path = os.path.join(FilesModule.QUEUED_DIR, fileName)
            doing_path = os.path.join(FilesModule.DOING_DIR, fileName)
            shutil.move(queued_path, doing_path)
            print(f"Moved to doing: {doing_path}")

            currentTime = datetime.now();
            formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
            outputDir = os.path.join(FilesModule.DONE_DIR, formattedTime)
            result = self.splitPdf(doing_path, outputDir);
            if (result):
                print(f"Successfully processed {result} files");
                print("Moving files to Done.")
                shutil.move(doing_path, outputDir)
                print(f"Moved to done: {outputDir}")
            else:
                print("The process failed. The script stays active.");

