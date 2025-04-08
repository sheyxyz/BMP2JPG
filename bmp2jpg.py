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
