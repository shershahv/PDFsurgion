# 🎯 Project Goal
# Create a command-line tool that:
# Opens and reads PDF files
# Extracts and searches text
# Merges, splits, and saves PDF files
# Displays metadata
# All using functions, without classes or advanced OOP features.


# from pypdf import PdfReader , PdfWriter

import pdf_core
import os



while True:
   doc_path = input("please insert pdf file path: " )
   
   options_text = "Please Select one of the options below: \n 1. Split-PDF \n 2. Merge-PDF \n 3. Extract-Text"
   print(options_text)
   user_selection = int(input("Your Choice: "))
   pdf = pdf_core.load_pdf(fr"{doc_path}")
   match user_selection:
      case 1:
         pdf_core.split_pdf(fr"{doc_path}")
      case 2:
         pass
      case 3:
         print(pdf_core.extract_text(pdf))
      
