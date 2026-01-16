from pathlib import Path

from behave import given, then, when
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


@given("the GitHub Pages site is reachable")
def step_site_reachable(context):
    response = context.page.goto(context.base_url, wait_until="networkidle")
    assert response is None or response.ok, f"Failed to reach {context.base_url}"


@when("I capture a screenshot of the landing page")
def step_capture_screenshot(context):
    screenshots_dir = Path(context.artifacts_dir) / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = screenshots_dir / "landing.png"
    context.page.screenshot(path=str(screenshot_path), full_page=True)


@when("I click the first available link")
def step_click_first_link(context):
    links = context.page.locator("a[href]")
    assert links.count() > 0, "No links found to click on the page"

    link = links.first
    try:
        with context.page.context.expect_page(timeout=3000) as new_page_info:
            link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        new_page.close()
    except PlaywrightTimeoutError:
        link.click()
        context.page.wait_for_load_state("domcontentloaded")


@then('the page should include the text "VLC"')
def step_page_contains_text(context):
    assert context.page.locator("text=VLC").count() > 0, "Expected text not found"
