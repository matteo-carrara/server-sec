echo This script show users allowed to login
awk -F: '$NF~/\/bash$/{print $1}' /etc/passwd

