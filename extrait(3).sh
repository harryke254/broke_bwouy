mkdir -p ~/phish/templates
cd ~/phish/templates
# Gmail user: save each "reset password" email by hand as .eml, then:
for f in ~/phish/templates/*.eml; do
  python3 - <<'EOF' "$f"
import sys, email
from email import policy
msg = email.message_from_file(open(sys.argv[1]), policy=policy.default)
html = msg.get_body(preferencelist=('html',)).get_content()
open(sys.argv[1].replace('.eml','.html'),'w').write(html)
EOF
done