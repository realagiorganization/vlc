import os
import re
from pathlib import Path

from playwright.sync_api import sync_playwright


ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"


def _safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", name).strip("_") or "scenario"


def before_all(context):
    context.base_url = os.environ.get("BASE_URL", "https://realagiorganization.github.io/vlc/")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    context.artifacts_dir = ARTIFACTS_DIR


def before_scenario(context, scenario):
    video_dir = context.artifacts_dir / "videos" / _safe_name(scenario.name)
    video_dir.mkdir(parents=True, exist_ok=True)
    context.browser_context = context.browser.new_context(
        record_video_dir=str(video_dir),
        viewport={"width": 1280, "height": 720},
    )
    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "browser_context", None):
        context.browser_context.close()


def after_all(context):
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()
