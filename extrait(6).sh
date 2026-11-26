sudo apt install -y php php-fpm
sudo a2enmod php* && sudo systemctl restart apache2
sudo mkdir -p /var/www/html/phish/{facebook,instagram,tiktok,twitter}
# place cloned HTML as clone.html in each folder