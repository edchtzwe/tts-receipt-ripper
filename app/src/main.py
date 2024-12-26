from services.PdfModule import PdfModule

class Main:
    def execute(self):
        print("Ready to process...");
        pdfUnit = PdfModule();
        while True:
            pdfUnit.processFiles();

app = Main();
app.execute();
