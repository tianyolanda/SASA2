import os
from PIL import Image

def crop_images_in_directory(input_dir, output_dir, x1, x2, y1, y2):
    """
    裁剪输入文件夹中的所有图像并保存到输出文件夹
    
    参数:
        input_dir: 输入文件夹路径
        output_dir: 输出文件夹路径
        x1, x2: 水平裁剪范围 (x1 < x2)
        y1, y2: 垂直裁剪范围 (y1 < y2)
    """
    # 确保输出文件夹存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_dir):
        try:
            # 构建完整的文件路径
            input_path = os.path.join(input_dir, filename)
            
            # 只处理图像文件（可以根据需要添加更多扩展名）
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # 打开图像
                with Image.open(input_path) as img:
                    # 裁剪图像
                    cropped_img = img.crop((x1, y1, x2, y2))
                    
                    # 构建输出路径
                    output_path = os.path.join(output_dir, filename)
                    
                    # 保存裁剪后的图像
                    cropped_img.save(output_path)
                    print(f"已裁剪并保存: {filename}")
                    
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {e}")

# 使用示例
if __name__ == "__main__":
    # 设置输入和输出文件夹路径
    input_directory = "dir/"      # 原始图像文件夹
    output_directory = "dir_new/" # 裁剪后图像保存文件夹
    
    # 设置裁剪范围 (左, 上, 右, 下)
    crop_x1 = 90  # 左边界
    crop_x2 = 1400  # 右边界
    crop_y1 = 830  # 上边界
    crop_y2 = 2000  # 下边界
    
    # 调用函数进行裁剪
    crop_images_in_directory(input_directory, output_directory, 
                           crop_x1, crop_x2, crop_y1, crop_y2)
