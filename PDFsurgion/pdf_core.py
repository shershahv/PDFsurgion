import pypdf


def load_pdf (file_path) :
    try:
        return pypdf.PdfReader(file_path)
    except FileNotFoundError as e:
        print(f"File not FOund error : {e}")
        exit()


def get_page_count(reader):
    return reader.get_num_pages()

def extract_text(reader, page_number=None) :
    pages = reader.pages
    text = ""
    for page in pages:
        text += page.extract_text()
    
    return text


def extract_images(reader, page_number=None) :
    pdf = reader.pages
    images_data = []
    for page in pdf:
        for image in page.images:
            images_data.append(image.data)
    
    return images_data
   
def get_metadata(reader):
    return reader.metadata


def merge_pdfs(file_paths, output_path=None):
    try:
        # merger = pypdf.PdfWriter()
      
        with open (output_path or "merged_pdf.pdf", "wb") as f :
            merger = pypdf.PdfWriter()
            for file in file_paths:
                merger.append(file)
            
            merger.write(f)
                
        print("Success merging")
    except FileNotFoundError as e:
        print("file not found error")
    
  
def split_pdf(file_path, output_dir=None):
    
    pdf_reader = load_pdf(file_path)
    page_count = get_page_count(pdf_reader)

    counter = 0
    
    
    for i in range(page_count):
        counter += 1
        pdf_writer = pypdf.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[i])
        pdf_writer.write(f"page {counter}.pdf")
        pdf_writer.close()
    
    
    
    
    
    
    

    
    
    
    
    
    
# pdf = load_pdf("sample2.pdf")

# pages = pdf.pages


# text = extract_text(pdf)
# # print(text)


# images = extract_images(pdf)
# # print(pages[0].images[0].data)
# print(len(images))

# def ExportImages(extractedImages):
#     image_count = 1
#     for image in images:
    
#         image_name = str(image_count) + ".png"
#         with open(image_name, "wb") as data:
#             data.write(image)
#         image_count += 1
    
    
# files_path = ["samplew.pdf","sample2.pdf"]
# # output = "new_merger155.pdf"
# merge_pdfs (files_path)

split_pdf("sample.pdf")
