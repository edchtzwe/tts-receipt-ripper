from PyPDF2 import PdfReader, PdfWriter
from services.FilesModule import FilesModule

class PdfModule:
    filesModule = None;

    def __init__(self):
        self.filesModule = FilesModule();

    def writePdf(self, outputPdfPath, writer):
        try:
            with open(outputPdfPath, "wb") as outputFile:
                writer.write(outputFile)
                print(f"Saved: {outputPdfPath}")

                return 1;
        except Exception as e:
            print(f"Failed to save {outputPdfPath} with Errors: {e}");

            return 0

    def splitPdf(self, filePath, outputDir):
        if (not len(filePath)):
            return 0;

        reader = PdfReader(filePath)
        if (not len(reader.pages)):
            return 0;

        self.filesModule.createOutputDir(outputDir);

        result = 0;
        for i, page in enumerate(reader.pages):
            pageText = page.extract_text()
            if (not len(pageText)):
                pass

            pageCount = f"page_{i+1}";
            saveFileName = self.filesModule.getSaveFileName(pageText, pageCount);

            writer = PdfWriter()
            writer.add_page(page)
            outputPdfPath = self.filesModule.getOutputPdfPath(outputDir, saveFileName);

            result += self.writePdf(outputPdfPath, writer);

        return result;
