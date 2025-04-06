#Write a program to manipulate pdf files using pyPDF. 
# Your programs should be able to merge multiple pdf files,
#into a single pdf. You are welcome to add more functionalities.
#pydf is a free and open source pure-python pdf library
#capable of splitting, merging, cropping and transforming the pages 
#of pdf files. It can also add custom data,
#viewing options, and passwords to pdf files. pypdf can retrieve text and metadata from pdfs as well.


import os
from pypdf import PdfWriter
merger = PdfWriter()
print("Welcome to the PDF Merger program!")
user_folder = input(r"Copy - paste the folder path containing PDF files: ").strip()
files = sorted(f for f in os.listdir(user_folder) if f.endswith('.pdf'))
print("The following PDF files will be merged:")
def pdfmerger(user_folder, files):
   for file in files:
      print(file)
      merger.append(os.path.join(user_folder, file))
   merger.write(os.path.join(user_folder, "MergedPDF.pdf"))
   print("PDF files have been merged successfully!")
   print("MergedPDF.pdf has been created in the specified folder.")
   print("Thank you for using the PDF Merger program!")
   print("Goodbye!")

pdfmerger(user_folder, files)

