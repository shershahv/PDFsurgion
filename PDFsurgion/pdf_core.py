import pypdf


def load_pdf (file_path) :
    return pypdf.PdfReader(file_path)
   


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


    
    
    
    
    
    
    
pdf = load_pdf("sample2.pdf")

pages = pdf.pages


text = extract_text(pdf)
# print(text)


images = extract_images(pdf)
# print(pages[0].images[0].data)
print(len(images))

def ExportImages(extractedImages):
    image_count = 1
    for image in images:
    
        image_name = str(image_count) + ".png"
        with open(image_name, "wb") as data:
            data.write(image)
        image_count += 1
    
    
# ExportImages(images)

# print(get_metadata(pdf).author)
metadata = get_metadata(pdf)
# for key in metadata.keys():
#     print(key)
    
# for value in metadata.values():
#     print(value)
    
# for key, value in metadata.items():
#     print(f"{key} : -> {value}")
    
    
# print(type(metadata.items()))

# print(metadata.items())

items_list = ["hi", "hello", "How are yoy"]

hi, hello, greetings = items_list

print(hi,hello, greetings, end="\n \n")