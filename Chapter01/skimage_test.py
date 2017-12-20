from skimage import data, io, filters

image = data.coins()
io.imshow(image)
edges = filters.sobel(image)
io.imshow(edges)
io.show()