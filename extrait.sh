# Sherlock — checks 400+ sites for a username
git clone https://github.com/sherlock-project/sherlock.git ~/tools/sherlock
cd ~/tools/sherlock && python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && deactivate && cd ~

# Maigret — richer profile (bio, avatar, uid, extra fields)
pip3 install maigret

# social-analyzer — API-free metadata
pip3 install social-analyzer

# WhatsMyName — accounts DB (Sherlock can consume it)
git clone https://github.com/webbreacher/whatsmyname.git ~/tools/whatsmyname

# Instagram / TikTok quick scrapers
pip3 install instaloader tiktok-scraper

# Holehe — email→registered-services (bonus if you also have an email)
pip3 install holehe