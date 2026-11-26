#!/usr/bin/env python3
"""Aggregate every public detail about a username across social platforms."""
import json, subprocess, sys, os, datetime

PLATFORMS = [
    "facebook","instagram","twitter","tiktok","linkedin","github",
    "reddit","pinterest","snapchat","youtube","telegram","twitch",
    "tumblr","medium","threads","discord"
]

def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=300).stdout
    except Exception as e:
        return f"ERROR: {e}"

def main(username):
    out_dir = os.path.expanduser(f"~/osint/{username}")
    os.makedirs(out_dir, exist_ok=True)
    report = {"username": username, "generated": str(datetime.datetime.now())}

    # --- Sherlock ---
    print("[+] Sherlock ...")
    sh = run(["sherlock", username, "--print-found", "--json", f"{out_dir}/sherlock.json"])
    report["sherlock_raw"] = sh.strip().splitlines()

    # --- Maigret (richer) ---
    print("[+] Maigret ...")
    mg = run(["maigret", username, "--json", "simple", "--folderoutput", out_dir])
    try:
        with open(f"{out_dir}/{username}.json") as f:
            report["maigret"] = json.load(f)
    except Exception:
        report["maigret_raw"] = mg

    # --- WhatsMyName filtered by platform ---
    print("[+] WhatsMyName ...")
    wmn = run(["python3", os.path.expanduser("~/tools/whatsmyname/wmn-data-schema.json")])  # optional

    # --- Instagram deep dump ---
    print("[+] Instagram ...")
    try:
        ig = run(["instaloader", "--no-pictures", "--no-videos", "--no-metadata-json",
                  "--no-captions", "--no-compress-json", username])
        report["instagram"] = ig
    except Exception as e:
        report["instagram"] = str(e)

    # --- TikTok ---
    print("[+] TikTok ...")
    try:
        tt = run(["tiktok-scraper", "user", username, "-j"])
        report["tiktok"] = json.loads(tt) if tt.strip().startswith("[") else tt
    except Exception:
        report["tiktok"] = "not found"

    with open(f"{out_dir}/report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    print(f"\n[✓] Full report: {out_dir}/report.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 osint_user.py <username>")
    main(sys.argv[1])
