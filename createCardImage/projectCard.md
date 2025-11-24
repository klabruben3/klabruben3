# 🖼️ Project Card Generator (Python + Playwright)

This tool generates clean, consistent, high-quality project preview cards for <strong>GitHub READMEs</strong>.
Instead of manually taking screenshots or fighting Markdown’s styling limitations, this script renders a styled HTML card and exports it as a PNG image using Playwright.

Perfect for portfolio READMEs, project showcases, or anywhere you want polished visuals.

## 🚀 Features

- Interactive CLI workflow

  - Enter a project name, description, tech stack, and image path/link.

- Auto-generated project card

  - Your input is placed into a styled HTML template.

- High-resolution screenshots

  - Uses Playwright with device_scale_factor=3 for crisp results.

- Cropping to the exact .card element

  - No extra whitespace — only the card is captured.

- Reusable + customizable
  - All styles live in utils/style.py and can be easily modified.

## 📦 Project Structure

```
project/
│
├── main.py                # Entry point
├── utils/
│   ├── data.py            # Input collection + HTML generation
│   └── style.py           # CSS + card dimensions
│
└── project_media/         # Where generated cards are saved
```

## 🛠️ Requirements

- Python 3.7+

- Playwright

Install Playwright and its browser binaries:

```bash
pip install playwright
playwright install chromium
```

## ▶️ Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/project-card-generator.git
cd project-card-generator
```

### Run the script

```bash
python main.py
```

### Follow the prompts:

1. Enter project name

2. Enter project description

3. Enter tech stack items (type x to stop)

4. Enter image path or URL

5. Name your screenshot

### The script will:

1. Generate the HTML card

2. Render it in a Chromium viewport

3. Screenshot only the .card element

Save it in `./project_media/`

## ✨ Example Output

<img alt="Personal Portfolio" title="My devfolio Card" src="../project_media/devfolio.png" width=250/>
<img alt="Pixel Kombat" title="Pixel Kombat ~ visit my repo" src="../project_media/pixel-kombat.png" width=250 />
<img alt="Clean chase" title="Clean chase Animation" src="../project_media/clean-chase.png" width=250 />

## 🧩 How It Works

### Rendering

The script builds HTML using your input, then Playwright loads it in a headless Chromium page:

```
page = browser.new_page(
viewport={"width": cardW, "height": cardW},
device_scale_factor=3
)
page.set_content(html)
```

### Cropping Only the Card

Instead of screenshotting the whole page:

```
card = page.query_selector(".card")
card.screenshot(path=f"./project_media/{image}.png", omit_background=True)
```

This ensures a clean, perfectly-fitted image.

## 🎯 Why I Built This

GitHub’s Markdown ignores `<style>` tags and most HTML formatting.
So embedding “designed” cards directly in README.md is impossible.

This tool solves that by generating clean images you can embed anywhere — no CSS required.
