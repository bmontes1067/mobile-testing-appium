"""
Descarga las apps de demo de Sauce Labs.
Uso:
    python scripts/download_apps.py --platform android
    python scripts/download_apps.py --platform ios
    python scripts/download_apps.py --platform both
"""

import os
import sys
import json
import argparse
import urllib.request

APPS_DIR = "apps"

GITHUB_REPOS = {
    "android": {
        "repo": "saucelabs/my-demo-app-android",
        "asset_suffix": ".apk",
        "exclude": "androidTest",
        "dest": "apps/my-demo-app-android.apk",
    },
    "ios": {
        "repo": "saucelabs/my-demo-app-ios",
        "asset_suffix": ".zip",
        "exclude": None,
        "dest": "apps/my-demo-app-ios.app.zip",
    },
}


def get_latest_asset_url(repo: str, asset_suffix: str, exclude: str = None) -> str:
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(api_url, headers={"User-Agent": "qa-portfolio-downloader"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    assets = data.get("assets", [])
    for asset in assets:
        if asset["name"].endswith(asset_suffix):
            if exclude and exclude in asset["name"]:
                continue
            return asset["browser_download_url"]
    raise RuntimeError(f"No se encontró asset '{asset_suffix}' en la última release de {repo}")


def download(platform: str):
    info = GITHUB_REPOS[platform]
    dest = info["dest"]
    if os.path.exists(dest):
        print(f"[{platform}] Ya existe: {dest} — omitiendo.")
        return
    os.makedirs(APPS_DIR, exist_ok=True)
    print(f"[{platform}] Consultando GitHub API...")
    try:
        url = get_latest_asset_url(info["repo"], info["asset_suffix"], info.get("exclude"))
    except Exception as e:
        print(f"[{platform}] ❌ {e}")
        sys.exit(1)
    print(f"[{platform}] Descargando {url} ...")
    urllib.request.urlretrieve(url, dest)
    size_mb = os.path.getsize(dest) / (1024 * 1024)
    print(f"[{platform}] ✅ {dest} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", choices=["android", "ios", "both"], default="both")
    args = parser.parse_args()
    targets = ["android", "ios"] if args.platform == "both" else [args.platform]
    for p in targets:
        download(p)
