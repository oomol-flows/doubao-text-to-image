#region generated meta
import typing
class Inputs(typing.TypedDict):
    prompt: str
class Outputs(typing.TypedDict):
    image_url: typing.NotRequired[str]
    image_path: typing.NotRequired[str]
#endregion

from oocana import Context
import requests
import os
from datetime import datetime

async def main(params: Inputs, context: Context) -> Outputs:
    """
    Generate images from text descriptions using Doubao text-to-image API

    Parameters:
        params: Input parameter dictionary containing prompt
        context: OOMOL context object

    Returns:
        Dictionary containing image_url and image_path
    """

    prompt = params["prompt"]

    # Get OOMOL token for authentication
    api_key = await context.oomol_token()

    # API endpoint
    url = "https://fusion-api.oomol.com/v1/doubao-text-to-image-seedream/action/generate"

    # Request headers
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    # Request body
    payload = {
        "prompt": prompt
    }

    try:
        # Make POST request to generate image
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        # Parse response
        result = response.json()

        # Extract image URL from response
        # API returns: {'success': True, 'data': [{'url': '...', 'size': '...'}]}
        if "data" in result and isinstance(result["data"], list) and len(result["data"]) > 0:
            image_url = result["data"][0]["url"]
        elif "data" in result and "image_url" in result["data"]:
            image_url = result["data"]["image_url"]
        elif "image_url" in result:
            image_url = result["image_url"]
        else:
            raise ValueError(f"Unexpected API response format: {result}")

        # Download the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        # Create output directory if it doesn't exist
        output_dir = "/oomol-driver/oomol-storage/text-to-image"
        os.makedirs(output_dir, exist_ok=True)

        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"generated_{timestamp}.jpeg"
        image_path = os.path.join(output_dir, image_filename)

        # Save image to local file
        with open(image_path, "wb") as f:
            f.write(image_response.content)

        # Preview the generated image using local file path
        context.preview({
            "type": "image",
            "data": f"file://{image_path}"
        })

        return {
            "image_url": image_url,
            "image_path": image_path
        }

    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to generate image: {str(e)}")
