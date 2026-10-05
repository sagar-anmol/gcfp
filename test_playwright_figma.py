import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            permissions=['clipboard-read', 'clipboard-write']
        )
        page = await context.new_page()
        print("Navigating to FigJam board...")
        try:
            await page.goto("https://www.figma.com/board/DVhtw8sjzvom28M7CU8kY7/plan", timeout=30000)
            await page.wait_for_timeout(5000)
            title = await page.title()
            print(f"Page title: {title}")
            url = page.url
            print(f"Current URL: {url}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

asyncio.run(main())
