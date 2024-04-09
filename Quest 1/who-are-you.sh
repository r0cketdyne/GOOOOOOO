
curl https://platform.zone01.gr/assets/superhero/all.json | jq -r "(.[] | select(.id == 70))" | jq ".name" 




