import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/opt/google/chrome/chrome",
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--no-sandbox',
                '--disable-setuid-sandbox'
            ]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (X-UA-Compatible; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            permissions=['clipboard-read', 'clipboard-write']
        )
        page = await context.new_page()
        print("Navigating to FigJam board with stealth settings...")
        try:
            resp = await page.goto("https://www.figma.com/board/DVhtw8sjzvom28M7CU8kY7/plan", timeout=30000)
            print(f"Status: {resp.status}")
            await page.wait_for_timeout(6000)
            title = await page.title()
            print(f"Page title: {title}")
            print(f"URL: {page.url}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

asyncio.run(main())
