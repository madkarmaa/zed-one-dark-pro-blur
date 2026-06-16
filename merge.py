import json
from pathlib import Path
from typing import Any

THEMES_DIR = Path("themes/").resolve()
TEMP_THEMES_DIR = Path("themes/tmp/").resolve()

FINAL_THEME = THEMES_DIR / "one-dark-pro-blur.json"
BASE_THEME = TEMP_THEMES_DIR / "base.json"
TEMP_THEMES = [
    theme
    for theme in TEMP_THEMES_DIR.iterdir()
    if theme.is_file() and theme.suffix == ".json" and theme != BASE_THEME
]


def patch_theme_name(theme_file: Path) -> Any:
    json_data = json.loads(theme_file.read_text())
    json_data["name"] = theme_file.stem.replace("-", " ")
    return json_data


def main() -> None:
    base_theme_data = json.loads(BASE_THEME.read_text())

    for theme in TEMP_THEMES:
        patched_data = patch_theme_name(theme)
        del patched_data["$schema"]

        base_theme_data["themes"].append(patched_data)

    FINAL_THEME.write_text(json.dumps(base_theme_data, indent=4))


if __name__ == "__main__":
    main()
