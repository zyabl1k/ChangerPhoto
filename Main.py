from PIL import Image
import os
import random

input_folder = "./input"
output_folder = "./output"

# создаем папку output, если ее нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# проходимся по всем файлам в папке input
for file_name in os.listdir(input_folder):
    # проверяем, что это файл изображения
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        # открываем изображение
        image_path = os.path.join(input_folder, file_name)
        image = Image.open(image_path)

        # изменяем хэш
        new_hash = random.randint(0, 999999999)
        image.info["hash"] = str(new_hash)

        # добавляем 3 рандомных пикселя с зеленым цветом и увеличенным размером
        for i in range(3):
            x = random.randint(0, image.width - 1)
            y = random.randint(0, image.height - 1)
            color = (0, 255, 0)  # зеленый цвет
            image.putpixel((x, y), color)

            # увеличиваем размер пикселя в 2 раза
            image.putpixel((x+1, y), color)
            image.putpixel((x, y+1), color)
            image.putpixel((x+1, y+1), color)

        # сохраняем измененное изображение в папку output
        output_path = os.path.join(output_folder, file_name)
        image.save(output_path)