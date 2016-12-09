# ImageFile.LOAD_TRUNCATED_IMAGES = True
#
# size = 128, 128
#
# for infile in glob.glob("static/images/*.jpg"):
#     file, ext = os.path.splitext(infile)
#     im = Image.open(infile)
#     im.thumbnail(size)
#     im.save(file + ".thumbnail", "JPEG")

frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
print 'ok'