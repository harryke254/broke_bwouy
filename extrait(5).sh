sudo apt install -y postfix opendkim opendkim-tools
sudo dpkg-reconfigure postfix      # Internet Site, your FQDN
sudo opendkim-genkey -b 2048 -d yourdomain.com -s mail
sudo mv mail.private /etc/opendkim/keys/yourdomain.com/mail.private
sudo systemctl restart opendkim postfix
# Publish the TXT from /etc/opendkim/keys/yourdomain.com/mail.txt as mail._domainkey