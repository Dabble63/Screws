from PIL import Image, ImageDraw, ImageFont

def create_icon(size, filename):
    # Create image with blue background
    img = Image.new('RGB', (size, size), color='#0056b3')
    draw = ImageDraw.Draw(img)
    
    # Calculate font size (about 40% of image size)
    font_size = int(size * 0.4)
    
    # Try to use a nice font, fall back to default
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", font_size)
        except:
            # Use default font if Arial not found
            font = ImageFont.load_default()
    
    # Draw "HW" text in white, centered
    text = "HW"
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]  # Adjust for baseline
    
    # Draw text
    draw.text((x, y), text, fill='white', font=font)
    
    # Save as PNG
    img.save(filename, 'PNG')
    print(f"Created {filename} ({size}x{size})")

# Create both icons
create_icon(192, 'icon-192.png')
create_icon(512, 'icon-512.png')

print("Icons created successfully!")
