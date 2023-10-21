import aspose.slides as slides

ppt_file = r"C:\Users\lucky\Downloads\Chapter_2_V7.01.ppt"

# Load presentation
pres = slides.Presentation(ppt_file)

# Create PDF options
options = slides.export.PdfOptions()

# Include hidden slides
options.show_hidden_slides = True

# Save PPTX as PDF
pres.save("pptx-to-pdf-hidden-slides.pdf", slides.export.SaveFormat.PDF, options)