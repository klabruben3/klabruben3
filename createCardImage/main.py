from playwright.sync_api import sync_playwright

from utils.data import collectData, createHtml
from utils.style import cardW

if __name__ == "__main__":
    reset = "y"

    with sync_playwright() as p:
        browser = p.chromium.launch()

        while reset == "y":
            projectData = collectData()
            html = createHtml(projectData)

            # Chose what to store the png as
            image = input("\nPut a name on the screenshot: ")

            page = browser.new_page(viewport={"width": cardW, "height": cardW},
                                    device_scale_factor=3)
            page.set_content(html)
            card = page.query_selector(".card")
            card.screenshot(
                path=f"./project_media/{image}.png", omit_background=True)

            print(
                "\033[32mThe screen has been shot, I REPEAT, the screen has been shot!\033[0m")
            reset = input("You wanna take another shot? (y / n): ").lower()

    print("GoodBye!")
