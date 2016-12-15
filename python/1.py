from PIL import Image #python3 加载图像库
t = Image.new('L',(100,100),color = 100)
t.save('2.jpg')
print(t)
