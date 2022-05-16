jq '.[0:100]' offline_.json > off_pt1.json
jq '.[100:200]' offline_.json > off_pt2.json
jq '.[200:300]' offline_.json > off_pt3.json
jq '.[300:400]' offline_.json > off_pt4.json
jq '.[400:500]' offline_.json > off_pt5.json
jq '.[500:600]' offline_.json > off_pt6.json
jq '.[600:]' offline_.json > off_pt7.json