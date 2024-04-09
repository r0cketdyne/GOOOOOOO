
curl https://platform.zone01.gr/assets/superhero/all.json | jq -r "(.[] | select(.id == 170))" | jq ".name" 
curl https://platform.zone01.gr/assets/superhero/all.json | jq -r "(.[] | select(.id == 170))" | jq ".powerstats.power" 
curl https://platform.zone01.gr/assets/superhero/all.json | jq -r "(.[] | select(.id == 170))" | jq ".appearance.gender" 
 

