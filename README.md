# Object-Recognition-Airflow
A collection of notebooks and data, for loading images and recognizing the objects in the image.
Will be adding things.

## Body Editor Tool

This tool allows you to edit an image to give a person a fit, athletic body using AI (OpenAI DALL-E).

### Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

### Usage

1. **Prepare your image**: Ensure your image is a square PNG (less than 4MB) for best results with DALL-E 2. If not, the script might fail or OpenAI might reject it.

2. **Create a mask**:
   This script creates a mask that preserves the head (top 25%) and lets the AI regenerate the body (bottom 75%).
   ```bash
   python create_body_mask.py --input your_photo.png --output mask.png --percent 25
   ```
   Adjust `--percent` if the head takes up more or less space.

3. **Edit the image**:
   ```bash
   python edit_image.py --input your_photo.png --mask mask.png --prompt "a fit, athletic guy's body with 6 pack abs" --output result.png
   ```

4. **Check the result**: The edited image will be saved to `result.png`.
