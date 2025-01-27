from PIL import Image
import os

# Go through every jpg, png, webp, jpeg, JPG files in the "org" directory
for file in os.listdir("org"):
#    if file.endswith((".jpg", ".png", ".webp", ".jpeg", ".JPG")):
    if file.endswith((".jpeg", ".JPG")):
        # Construct the full file path
        file_path = os.path.join("org", file)
        
        # Open the image
        img = Image.open(file_path)
        
        # Show the image dimensions
        width, height = img.size
        
        # Print file size in kilobytes
        file_size_kb = int(os.path.getsize(file_path) / 1024)
        print(f"Image: {file}, Size: {file_size_kb}K, Width: {width}, Height: {height}")
        
        # If the file is a PNG, save it as a JPG
        if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".JPG"):
            new_file = file.rsplit('.', 1)[0] + ".jpg"
            img = img.convert("RGB")  # Convert to RGB mode
            img.save(new_file, quality=85, optimize=True)
            file_size_kb_new = int(os.path.getsize(new_file) / 1024)
            print(f"New Image: {new_file}, New Size: {file_size_kb_new}K")
        else:
            # Save the image with optimized quality
            img.save(file, quality=85, optimize=True)
            file_size_kb_new = int(os.path.getsize(file_path) / 1024)
            print(f"New Size: {file_size_kb_new}K")
        
        print("")