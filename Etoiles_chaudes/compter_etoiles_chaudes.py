from PIL import Image

print("----  Compter les étoiles chaudes ---------")
img = Image.open('C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Etoiles_chaudes\\ciel.png')
print(img.format, img.size, img.mode)
pix = img.load()
#print(type(pix))

width,height = img.size
print(f"{width} / {height}")
pixel_values = list(img.getdata())
#print(pixel_values)
#print(type(pixel_values[0]))

cnt=0
for rgb_pix in pixel_values:
    #print(rgb_pix)
    red,green,blue = rgb_pix
    #print(f"{red} / {green} / {blue}")
    if blue > red and blue > green:
        cnt+=1

print(f"Nombre d'étoiles chaudes: {cnt}")