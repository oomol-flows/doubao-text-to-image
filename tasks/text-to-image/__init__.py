#region generated meta
import typing
class Inputs(typing.TypedDict):
    prompt: str
class Outputs(typing.TypedDict):
    image_url: typing.NotRequired[str]
#endregion

from oocana import Context
import requests

async def main(params: Inputs, context: Context) -> Outputs:
    """
    Generate images from text descriptions using Doubao text-to-image API

    Parameters:
        params: Input parameter dictionary containing prompt
        context: OOMOL context object

    Returns:
        Dictionary containing image_url
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

        # Preview the generated image
        context.preview({
            "type": "image",
            "data": image_url
        })

        return {
            "image_url": image_url
        }

    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to generate image: {str(e)}")
