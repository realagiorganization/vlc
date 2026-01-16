# BDD GitHub Pages Smoke Test

This suite uses `behave` and Playwright to validate the GitHub Pages landing page,
record a click-through, and save artifacts (screenshots + video).

## Run locally

```bash
python3 -m pip install -r test/bdd/requirements.txt
python3 -m playwright install chromium
BASE_URL=https://realagiorganization.github.io/vlc/ python3 -m behave test/bdd/features
```

Artifacts are written to `test/bdd/artifacts/`.
