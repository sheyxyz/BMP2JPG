"""
BMP convert to JPG(在最高品質的前提下)

key point:
1. convert時要設定jpg的壓縮效率參數quality 為 100

2. convert時要將色彩子採樣設定為4:4:4

3. 壓縮比通常會在2:1 ~ 3:1之間(根據Huffman編碼和 DCT變換的效率而定)
比如12MB的bmp image通常壓縮成jpg image後會變成6MB ~ 4MB之間
但可能會根據圖片狀況有所不同，影響的可能包含:
a. 影像中有大量相似顏色，DCT變換壓縮效率更好
b. 影像本身就含有較多資料冗餘被Huffman編碼減少，使得壓縮效率更好

code ref: https://chatgpt.com/share/67c66832-7c30-8005-bfdd-7f172ba0e481
image transfer ref: https://chatgpt.com/share/67c66851-1eac-8005-8c27-6c954c5f9543

"""
import os
from PIL import Image

def read_path_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readline().strip()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def convert_bmp_to_jpg(input_folder="input", output_folder="output", quality=100):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".bmp"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            try:
                with Image.open(input_path) as img:
                    img = img.convert("RGB")  # 確保轉換為 RGB 模式，避免透明通道問題
                    # 儲存 JPG 時指定最高品質與 4:4:4 色彩子採樣
                    img.save(output_path, "JPEG", quality=quality, subsampling="4:4:4")
                    print(f"Converted: {input_path} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {input_path}: {e}")


if __name__ == "__main__":
    input_folder = read_path_from_file("input_path.txt")
    output_folder = read_path_from_file("output_path.txt")

    if input_folder and output_folder:
        convert_bmp_to_jpg(input_folder, output_folder)
    else:
        print("Invalid input or output folder path.")