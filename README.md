# HKLampPostParse

![](https://cdn-icons-png.flaticon.com/128/89/89069.png)
(Street icons created by Freepik)

[TOCM]

### Features
---
- This is a simple Python Flask API application to parse Hong Kong Lamp Post ID and returning GPS coordinates for further usage

- Returning district name and street name

### API Usage
---
######**Get Information by Lamp Post ID**
`lp?q=[LampPost ID]`

######**Update CSV**
`/lp?update`
It updates the csv file locally only if the file is older than 1 month. 
