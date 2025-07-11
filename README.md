# YouTube Content Generator

A simple Python application that generates comprehensive content for YouTube videos using AI. This tool helps content creators brainstorm ideas, create scripts, and expand their content across multiple platforms.

## Features

- **Title Generation**: Creates 10 catchy and attention-grabbing title ideas for your video topic
- **Thumbnail Ideas**: Generates detailed thumbnail descriptions based on the generated titles
- **Script Writing**: Creates a professional script for your specified video length
- **Twitter Thread**: Converts your video script into a viral Twitter thread with hashtags and emojis

## Prerequisites

- Python 3.6 or higher
- A Groq API key (free tier available)

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install groq
   ```

## Setup

1. Get your Groq API key from [Groq Console](https://console.groq.com/)
2. Set your API key as an environment variable:

   **Windows (Command Prompt):**

   ```cmd
   set GROQ_API_KEY=your_api_key_here
   ```

   **Windows (PowerShell):**

   ```powershell
   $env:GROQ_API_KEY="your_api_key_here"
   ```

## Usage

### Method 1: Run the batch file (Windows)

Double-click `run-me.bat` or run it from command prompt:

```cmd
run-me.bat
```

### Method 2: Run directly with Python

```bash
python app.py
```

### Interactive Process

1. Enter your video topic when prompted
2. Enter your desired video length in minutes
3. The application will generate:
   - 10 catchy title ideas
   - Detailed thumbnail descriptions
   - A complete video script
   - A Twitter thread based on the script

## Example Output

```
Please enter your video topic: AI and the Future of Work
Please enter your video length (in minutes): 5

Titles Ideas:
----------------
1. "AI Will Replace Your Job in 2025 (Here's How to Stay Ahead)"
2. "The SHOCKING Truth About AI and Your Career"
...

Thumbnail Ideas:
----------------
Thumbnail for "AI Will Replace Your Job in 2025":
- Split screen showing a robot and human handshake
- Bold red text overlay with "2025" prominently displayed
...

Suggested Script:
----------------
[0:00 - 0:15] Hook: "What if I told you that 40% of jobs..."
...

Twitter Thread:
----------------
🧵 THREAD: AI is reshaping the job market faster than ever! Here's what you need to know 👇
#AI #FutureOfWork #CareerTips
...
```

## File Structure

```
YouTube-Content-Generator/
├── app.py              # Main application file
├── groq_api.py         # Groq API integration
├── prompts.py          # AI prompts for different content types
├── run-me.bat          # Windows batch file for easy execution
└── README.md           # This file
```

## Customization

You can modify the prompts in `prompts.py` to:

- Change the writing style
- Adjust the tone of generated content
- Add specific requirements for your niche
- Modify the AI model used in `groq_api.py`

## API Model

This application uses the `llama-3.3-70b-versatile` model from Groq. You can change this in `groq_api.py` if needed.

## Troubleshooting

- **API Key Error**: Make sure your GROQ_API_KEY environment variable is set correctly
- **Import Error**: Ensure the `groq` package is installed with `pip install groq`
- **Rate Limits**: Groq has free tier limitations; consider upgrading for heavy usage

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
