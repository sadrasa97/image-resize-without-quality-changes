from PIL import Image
import io

def resize_to_approx_size(input_path, target_size_kb, output_path, tolerance=5):
    # Open the image
    with Image.open(input_path) as img:
        # Convert RGBA to RGB
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Use a binary search approach to find the quality factor that results in desired file size
        min_quality, max_quality = 10, 95
        while min_quality <= max_quality:
            mid_quality = (min_quality + max_quality) // 2

            # Save image to a bytes buffer to check the size
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=mid_quality)
            size_kb = len(buffer.getvalue()) // 1024

            # Adjust the quality factor based on current size
            if size_kb < target_size_kb - tolerance:
                min_quality = mid_quality + 1
            elif size_kb > target_size_kb + tolerance:
                max_quality = mid_quality - 1
            else:
                break

        # Save the image with the determined quality
        img.save(output_path, format='JPEG', quality=mid_quality)

#input_path =   # Replace with your image path
#output_path =   # Replace with your desired output path
#target_size_kb = 100  # Target file size in KB

#resize_to_approx_size(input_path, target_size_kb, output_path)

