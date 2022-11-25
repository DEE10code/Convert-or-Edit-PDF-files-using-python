from glob import glob

import pikepdf
from pikepdf import Pdf, PdfImage

def Rotate():
    act = int(input("How much degree you want to rotate - "))
    for i in old_pdf.pages:
        i.Rotate = act
        old_pdf.save("newRotated.pdf")

def Protected():
    owner = input("Enter the name of the Owner - ")
    passw = input("Enter the password - ")
    no_ext = pikepdf.Permissions(extract=False)
    old_pdf.save("protected_new.pdf",
                 encryption=pikepdf.Encryption(user=passw,
                                               owner=owner, allow=no_ext))


def Split_pages():
    for n, page_can in enumerate(old_pdf.pages):
        new_pdf = pikepdf.Pdf.new()
        new_pdf.pages.append(page_can)
        name = "Page" + str(n) + ".pdf"
        new_pdf.save(name)

def Reverse_oder():
    old_pdf.pages.reverse()
    old_pdf.save("Reverse.pdf")

def Cut_page():
    a = int(input('Which Page no you Want to copy '))
    b = int(input('Which Page no you Want to paste '))
    old_pdf.pages[a] = old_pdf.pages[b]
    old_pdf.save("Replace.pdf")

def Merge():
    ques = input("Enter those pdf file into the exe folder... "
                 "If yes press 'y', if no press 'n'")
    if ques == 'y':
        new_pdf = Pdf.new()
        for file in glob("*.pdf"):
            olds_pdf = Pdf.open(file)
            new_pdf.pages.extend(olds_pdf.pages)
    else:
        print("Sorry can't process")

def image_extract():
    ab = int(input('Enter the page no where the picture belong-'  ))
    page_1 = old_pdf.pages[ab]

    ques2 = input("If there is one picture press 'y' if no then press 'n' -" )
    if ques2 == 'y':
        aaa = (list(page_1.images.keys()))
        raw_image = page_1.images[aaa[0]]
        pdf_image = PdfImage(raw_image)
        pdf_image.extract_to(fileprefix="Your_image")
    elif ques2 == 'n':
        print((list(page_1.images.keys())))
        asu = input("Choose the image name and copy it (format - '/IM27' )- ")
        raw_image = page_1.images[asu]
        pdf_image = PdfImage(raw_image)
        pdf_image.extract_to(fileprefix="Your_image")
    else:
        print("Something went wrong")


# main code

print(
    "Please Notice if you want to do works with this function at first you have to put the file at the same "
    "destination where the exe or the .py program belongs")
pdf_name = input("Enter the pdf file name(like-anish.pdf)- ")
old_pdf = pikepdf.Pdf.open(pdf_name)

pdf = int(input("Which operation you want to perform - \n"
                "1.Rotate\n"
                "2.Protected\n"
                "3.Split_pages\n"
                "4.Reverse_oder\n"
                "5.Cut_page\n"
                "6.Merge\n"
                "7.image_extract\n"
                "Enter the operation you like by number -"))

if pdf == 1:
    Rotate()
elif pdf == 2:
    Protected()
elif pdf == 3:
    Split_pages()
elif pdf == 4:
    Reverse_oder()
elif pdf == 5:
    Cut_page()
elif pdf == 6:
    Merge()
elif pdf == 7:
    image_extract()
else:
    print("Wrong input")

# it will be updated