import glob
import os
from pathlib import Path

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from PIL import Image, ImageFont, ImageDraw
from pdf2image import convert_from_path
from pypdf import PdfMerger
import markdown

POSTER_DIR = Path("/Users/egomez/Library/CloudStorage/GoogleDrive-egomez@lco.global/Shared drives/Education/Space Quest/Plain Posters")
BASE_DIR = Path(__file__).parent.resolve()

def find_thing_files():
    things = []
    path = BASE_DIR / "content" / "articles"
    for f in path.glob("*.md"):
        data = f.read_text(encoding='utf-8')
        md = markdown.Markdown(extensions=['meta'])
        md.convert(data)
        things.append(md.Meta)
    return things

def write_qr_codes(things):
    for thing in things:
        poster_files = []
        nam_files = []
        url = "https://spacequest.uk/" + thing['slug'][0]
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(url)

        qrimg = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        qrimg = qrimg.resize((1000,1000), Image.Resampling.LANCZOS)

        poster_path =  "{}*.pdf".format(thing['slug'][0].capitalize())
        files = POSTER_DIR.glob(poster_path)
        font1 = ImageFont.truetype("/Users/egomez/Library/Fonts/Inconsolata-VariableFont_wdth,wght.ttf", 300)
        font1.set_variation_by_name('Condensed Medium')
        # font2 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Futura.ttc", 400)
        if not files:
            print(f"Could not find poster for {thing['slug'][0]}")
            continue
        for poster_file in files:
            images = convert_from_path(poster_file)
            path = Path(poster_file)
            poster = images[0]
            back_im = poster.copy()
            x, y = back_im.size
            back_im.paste(qrimg, (150, y-1250))

            draw = ImageDraw.Draw(back_im)
            draw.text((x/2+250, y-600), f"spacequest.uk/{thing['slug'][0]}", (0, 0, 0), font=font1)
            # if thing['id'][0] < 10:
            #     draw.text((x-1250, 1250), str(thing['id'][0]), (37,36,67), font=font2)
            # else:
            #     draw.text((x-1350, 1250), str(thing['id'][0]), (37,36,67), font=font2)

            save_path = BASE_DIR / "posters" / path.name
            back_im.save(save_path, quality=95)
            print('Created poster for {} in {}'.format(thing['title'][0], save_path))


        # print("Saved poster files. Making master file.")
        # for name, filegroup in {'nam':nam_files, 'poster':poster_files}.items():
        #     merger = PdfMerger()

        #     for pdf in filegroup:
        #         merger.append(pdf)

        #     save_path = settings.BASE_DIR / "posters" / f"{name}.pdf"
        #     merger.write(save_path)
        #     merger.close()

if __name__ == "__main__":
    things = find_thing_files()
    # print(things)
    write_qr_codes(things)