import requests
from ascii_magic import AsciiArt
from PIL import Image, ImageEnhance

def get_random_cat_image(api_key):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        'x-api-key': api_key
    }

    print("Getting your cat <3")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        cat_image_url = data[0]['url']
        print(cat_image_url)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return None

    return cat_image_url

def download_image(url, destination):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(destination, 'wb') as file:
            file.write(response.content)
        
        return destination

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return None

def isolate_cat(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGB mode if it's not already in that mode
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Enhance the contrast (optional)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(3.0)  # Increase the contrast

    # Extract the alpha channel
    alpha = img.split()[3]

    # Create a new image with a transparent background
    cat_with_transparent_bg = Image.new('RGBA', img.size, (0, 0, 0, 0))
    cat_with_transparent_bg.paste(img, (0, 0), alpha)

    # Resize the image to half the size
    resized_cat = cat_with_transparent_bg.resize((int(img.width / 12), int(img.height / 12)))

    # Save the isolated and resized cat image with a transparent background
    isolated_cat_path = 'isolated_resized_cat.png'
    resized_cat.save(isolated_cat_path)

    return isolated_cat_path

# Replace 'YOUR_API_KEY' with your actual API key
api_key = ''
# Call the function to get a random cat image
url = get_random_cat_image(api_key)

if url:
    downloaded_image = download_image(url, 'downloaded_cat.png')

    if downloaded_image:
        isolated_resized_cat_image = isolate_cat(downloaded_image)
        my_art = AsciiArt.from_image(isolated_resized_cat_image)
        
        # Set font size to make ASCII art smaller
        my_art.to_terminal(width_ratio=2, columns=100)