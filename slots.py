from PIL import Image, ImageDraw, ImageFont
import random

# Create a picture of 3 random icons on a transparent background
def get_symbols(width, height):
    # Take the original files, and pick 3 randomly
    filelist = ['money.png', 'happy.png', 'fear.png', 'devil.png']
    slotsresult = []
    for i in range(0, 3):
        slotsresult.insert(i, filelist[random.randint(0,3)])

    # Open each file and place them on the background image 70px apart
    offset = int(height / 2) - 35
    trans_bg = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    i = 100
    for filename in slotsresult:
        pic = Image.open("./pictures/"+filename, 'r')
        trans_bg.paste(pic, (i, offset))
        i += 70

    return {"layer":trans_bg, "images":slotsresult}

# Draw text on transparent background
def draw_text(text, width, height):
    font = ImageFont.truetype("./misc/KRAVT___.TTF", 40)
    size = font.getsize(text)

    # Create a new transparent image and place given text on it
    textbg = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    drawobj = ImageDraw.Draw(textbg)
    drawobj.text((int(width / 3), height - 48), text, font=font, fill="white")
    return textbg

def get_text(results):
    if results[0] == results[1] and results[1] == results[2]:
        if results[0] == "money.png":
            return "WOW!!"
        elif results[0] == "happy.png":
            return "Nice!"
        elif results[0] == "fear.png":
            return "Oh no.."
        else:
            return "...Ouch"

    return "Sorry."

def createpic():
    background = Image.open("./pictures/slotbg.png", 'r')
    bg_w, bg_h = background.size
    results = get_symbols(bg_w, bg_h)

    # Create a filter the size of the background of a random color
    transfilter = Image.new('RGBA', (bg_w, bg_h), (0, 0, 0, 0))
    color = (random.randint(77, 173), random.randint(77, 173), random.randint(77, 173), 160)
    colorfilter = Image.new('RGBA', (bg_w - 10, bg_h - 10), color)
    transfilter.paste(colorfilter, (5, 5))

    # Draw text based on results of slots
    text_to_display = get_text(results.get("images"))
    textbg = draw_text(text_to_display, bg_w, bg_h)

    # Place filter on the background, icons on the filter, then text on the very top
    transfilter = Image.alpha_composite(transfilter, textbg)
    background = Image.alpha_composite(background, transfilter)

    trans_bg = results.get("layer")
    Image.alpha_composite(background, trans_bg).save("img.png")
