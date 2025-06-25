from PIL import Image
import os

def resize_ico_to_48x48():
    """Resize the existing ICO file to 48x48"""
    
    # Open the existing ICO file
    ico_path = "code_to_vector_icon_minimal.ico"
    
    if not os.path.exists(ico_path):
        print(f"Error: {ico_path} not found!")
        return
    
    try:
        # Open the ICO file
        with Image.open(ico_path) as img:
            # Convert to RGBA if needed
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Resize to 48x48
            resized_img = img.resize((48, 48), Image.Resampling.LANCZOS)
            
            # Save as new ICO file with only 48x48 size
            resized_img.save("code_to_vector_icon_48x48.ico", "ICO")
            
            print("ICO file successfully resized to 48x48!")
            print("New file: code_to_vector_icon_48x48.ico")
            
            # Also save as PNG for verification
            resized_img.save("code_to_vector_icon_48x48_verification.png", "PNG")
            print("Verification PNG: code_to_vector_icon_48x48_verification.png")
            
    except Exception as e:
        print(f"Error processing ICO file: {e}")

if __name__ == "__main__":
    resize_ico_to_48x48() 