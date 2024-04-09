curl -s https://platform.zone01.gr/assets/superhero/all.json | jq -r "(.[] | select(.id == $HERO_ID))" | jq -r ".connections.relatives" | sed ':a;N;$!ba;s/\n/\\n/g'
