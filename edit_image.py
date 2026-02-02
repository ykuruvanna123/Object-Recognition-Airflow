import os
import sys
from openai import OpenAI
from PIL import Image
import argparse

def edit_image(input_path, mask_path, output_path, prompt):
    client = OpenAI()

    # Open the image and mask
    try:
        image = open(input_path, "rb")
        mask = open(mask_path, "rb")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    print(f"Editing image {input_path} with prompt: '{prompt}'...")

    try:
        response = client.images.edit(
            image=image,
            mask=mask,
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        image_url = response.data[0].url
        print(f"Image generated! URL: {image_url}")
        
        # Download the image
        import requests
        img_data = requests.get(image_url).content
        with open(output_path, 'wb') as handler:
            handler.write(img_data)
        
        print(f"Saved edited image to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edit an image using OpenAI DALL-E 2")
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--mask", required=True, help="Path to mask image (transparent area is what gets edited)")
    parser.add_argument("--output", default="output.png", help="Path to save output image")
    parser.add_argument("--prompt", default="a fit, athletic guy's body with 6 pack abs", help="Prompt for editing")

    args = parser.parse_args()
    
    # Check for API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    edit_image(args.input, args.mask, args.output, args.prompt)
