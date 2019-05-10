from PIL import Image,ImageFilter,ImageDraw
# im = Image.open("D:/a_pic/gakki.jpg")
# print(im.mode)

#获取模式
i1 = Image.open("yournameWB.jpg")
print(i1.mode)
print(i1.size)
print(i1.format)


# blur image
# blured = i1.filter(ImageFilter.BLUR)
# blured.save("yournameB.png")

# convert RGB image to grayscale image
# l1 = i1.convert('L')
# l1.save("yournameWB.jpg")

# can not convert L image to rgb
# ri = i1.convert('RGB')
# ri.show()


# crop image
# croped = i1.crop((100,100,500,500))
# croped.show()


# pixel1 = i1.getpixel((0,0))#(23, 35, 61)
# print(pixel1)
#i1.rotate(45).show()


#create a image
# img = Image.new('RGBA', (200, 200), 'white')
# idraw = ImageDraw.Draw(img)
#
# idraw.rectangle((10, 10, 100, 100), fill='blue')
#
# img.save('rectangle.png')

i1.thumbnail((125,125))
i1.save("thumbnail.png")
i1.show()
