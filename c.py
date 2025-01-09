import os

def count_files_in_folder(folder_path):
    try:
        # Kiểm tra nếu folder tồn tại
        if not os.path.exists(folder_path):
            print(f"Thư mục '{folder_path}' không tồn tại.")
            return 0

        # Lấy danh sách tất cả các tệp con trong folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        # Đếm số lượng tệp
        file_count = len(files)

        print(f"Số tệp con trong thư mục '{folder_path}': {file_count}")
        return file_count

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return 0

# Đường dẫn đến thư mục
folder_path = "Data/1500-2000"
count_files_in_folder(folder_path)
