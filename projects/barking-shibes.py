# Use a quotes API, e.g. https://api.quotable.io/quotes/random
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import requests

def fetch_doge_quote():
    # Fetch a random quote
    quote_response = requests.get("https://api.quotable.io/quotes/random")
    quote_data = quote_response.json()
    quote = quote_data['content']
    
    # Convert quote to Doge speech
    doged_quote = quote.replace('you', 'u').replace('are', 'r').replace('and', 'n').replace('is', 'iz').replace('to', '2').replace('for', '4')
    
    return doged_quote

def fetch_doge_image():
    # Fetch a random Doge image
    image_response = requests.get("http://shibe.online/api/shibes")
    image_data = image_response.json()
    doge_image_url = image_data[0]  # Get the first image URL
    
    return doge_image_url

def create_html(doged_quote, doge_image_url):
    # Create HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Doge Quote</title>
        <style>
            body {{
                text-align: center;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }}
            img {{
                width: 300px;
                height: auto;
            }}
            .quote {{
                font-size: 24px;
                margin: 20px;
                padding: 10px;
                border: 2px solid #ffcc00;
                border-radius: 10px;
                background-color: #fff;
            }}
        </style>
    </head>
    <body>
        <h1>Doge Quote</h1>
        <img src="{doge_image_url}" alt="Doge Image">
        <div class="quote">{doged_quote}</div>
    </body>
    </html>
    """
    
    # Write to an HTML file
    with open('doge_quote.html', 'w') as file:
        file.write(html_content)

def main():
    doged_quote = fetch_doge_quote()
    doge_image_url = fetch_doge_image()
    create_html(doged_quote, doge_image_url)

if __name__ == "__main__":
    main()
