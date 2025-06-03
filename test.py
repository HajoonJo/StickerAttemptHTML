img_path = r"D:\TSC stuff\Git Projects\ProjectSticker\BORIS.png"

try:
    with open(img_path, "rb") as f:
        print("Successfully opened the file using open()")
except FileNotFoundError:
    print("open() failed: file not found")
