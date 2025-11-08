# Doubao Text-to-Image Generator

A powerful OOMOL workflow project that generates high-quality images from text descriptions using the Doubao text-to-image API.

## Overview

This project provides a simple and efficient way to transform your creative text prompts into beautiful images. Whether you're a designer looking for inspiration, a content creator needing visuals, or anyone who wants to bring their ideas to life visually, this tool makes AI-powered image generation accessible and easy to use.

## Features

- **Text-to-Image Generation**: Convert any text description into a corresponding image
- **Automatic Image Storage**: Generated images are automatically saved locally with timestamped filenames
- **Real-time Preview**: View generated images immediately in the OOMOL interface
- **Simple Integration**: Easy to incorporate into your OOMOL workflows

## Functional Modules

### Text to Image Block

The core functionality of this project is provided by the **Text to Image** block, which:

- **Accepts Text Prompts**: Takes natural language descriptions of the image you want to create
- **Generates Images**: Uses the advanced Doubao AI model to create images from your descriptions
- **Returns Multiple Outputs**: Provides both the online image URL and local file path for flexibility
- **Handles Storage Automatically**: Saves generated images to `/oomol-driver/oomol-storage/text-to-image/` with unique filenames

#### Inputs

- **prompt** (string): A text description of the image you want to generate. Be as detailed and descriptive as possible for best results.
  - Example: "A serene mountain landscape at sunset with golden light"
  - Example: "A futuristic city with flying cars and neon lights"

#### Outputs

- **image_url** (string): The online URL where the generated image is hosted
- **image_path** (string): The local file path where the image has been saved on your system

## Usage

### Basic Workflow

1. **Add the Text to Image block** to your OOMOL workflow
2. **Enter your prompt** describing the image you want to generate
3. **Run the workflow** and wait for the image to be generated
4. **View the result** in the preview panel
5. **Access the image** using either the returned URL or local file path

### Example Use Cases

- **Creative Design**: Generate concept art and design inspiration
- **Content Creation**: Create unique images for blog posts, social media, or presentations
- **Prototyping**: Quickly visualize ideas without manual design work
- **Education**: Illustrate concepts and ideas in educational materials
- **Marketing**: Generate promotional visuals and marketing assets

## Installation

This project uses both Python and Node.js dependencies. To set up:

```bash
# Install all dependencies
npm install
poetry install --no-root
```

The installation is automatically handled when you load the project in OOMOL.

## File Structure

```
doubao-text-to-image/
├── tasks/
│   └── text-to-image/          # Main text-to-image generation task
│       ├── __init__.py          # Task implementation
│       └── task.oo.yaml         # Task configuration
├── flows/
│   └── test-text-to-image/     # Test workflow
│       └── flow.oo.yaml         # Flow configuration
├── package.oo.yaml              # OOMOL package configuration
├── pyproject.toml               # Python dependencies
├── package.json                 # Node.js dependencies
├── icon.png                     # Project icon
└── README.md                    # This file
```

## Technical Details

### Authentication

This project uses OOMOL's built-in token authentication system. The OOMOL token is automatically retrieved at runtime, so no manual API key configuration is required.

### API Endpoint

The project connects to the Doubao text-to-image API at:
```
https://fusion-api.oomol.com/v1/doubao-text-to-image-seedream/action/generate
```

### Storage Location

Generated images are stored in the OOMOL runtime storage directory:
```
/oomol-driver/oomol-storage/text-to-image/
```

Files are named with timestamps: `generated_YYYYMMDD_HHMMSS.jpeg`

### Dependencies

**Python**:
- `requests`: HTTP client for API communication
- `oocana`: OOMOL runtime context (pre-installed)

**Node.js**: Standard OOMOL runtime dependencies

### Error Handling

The block includes comprehensive error handling for:
- Network connection issues
- API request failures
- Invalid response formats
- File system operations

All errors are reported with clear, descriptive messages to help troubleshoot issues.

## Requirements

- OOMOL platform (latest version recommended)
- Internet connection for API access
- Write permissions to the OOMOL storage directory

## Support

For issues, questions, or feature requests, please refer to the OOMOL platform documentation or community resources.

## License

This project follows the OOMOL platform licensing terms.

---

**Version**: 0.0.1

**Icon**: 🖼️ Image generation icon

**Last Updated**: 2025
