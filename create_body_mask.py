from PIL import Image
import argparse

def create_mask(input_path, output_path, top_preserve_percent=20):
    try:
        img = Image.open(input_path).convert("RGBA")
        width, height = img.size
        
        # Calculate the split line
        split_y = int(height * (top_preserve_percent / 100))
        
        # Create a new image for the mask
        # The mask should be an RGBA image where the area to edit is fully transparent (alpha=0)
        # And the area to keep is fully opaque (alpha=255).
        # Wait, OpenAI docs say: "The transparent areas of the mask indicate where the image should be edited."
        
        # So we want the body (bottom part) to be transparent.
        # And the head (top part) to be opaque.
        
        # Create a mask array
        datas = img.getdata()
        new_data = []
        
        for y in range(height):
            for x in range(width):
                # We are iterating implicitly by creating a new list of pixels matching the size
                # But getdata() returns a flat list.
                # Let's do it with pixel access for clarity.
                pass
        
        # Faster way:
        # Create a fully transparent image
        mask = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        
        # Paste the top part of the original image (or just a black rectangle?)
        # OpenAI docs: "The mask should have transparent areas where you want the edit to happen."
        # The documentation says the mask needs to be a PNG.
        
        # Let's create an image that is fully transparent at the bottom, and opaque at the top.
        # But wait, the mask file itself doesn't need the original image content, just the alpha channel.
        # Actually, for OpenAI `image` + `mask`:
        # "Must be a valid PNG file, less than 4MB, and square."
        
        # Let's keep it simple:
        # Create a PNG where top 20% is OPAQUE (alpha 255) and bottom 80% is TRANSPARENT (alpha 0).
        # Color doesn't matter for the opaque part, usually. But let's make it white.
        
        final_mask = Image.new("RGBA", (width, height), (255, 255, 255, 0)) # Fully transparent start
        
        # Draw opaque rectangle at top
        from PIL import ImageDraw
        draw = ImageDraw.Draw(final_mask)
        # (x0, y0, x1, y1)
        draw.rectangle([(0, 0), (width, split_y)], fill=(255, 255, 255, 255))
        
        final_mask.save(output_path)
        print(f"Created mask at {output_path} with top {top_preserve_percent}% opaque.")
        
    except Exception as e:
        print(f"Error creating mask: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a simple mask for body editing")
    parser.add_argument("--input", required=True, help="Path to input image (to get dimensions)")
    parser.add_argument("--output", default="mask.png", help="Path to save mask")
    parser.add_argument("--percent", type=int, default=25, help="Percentage of top to preserve (head)")
    
    args = parser.parse_args()
    create_mask(args.input, args.output, args.percent)
