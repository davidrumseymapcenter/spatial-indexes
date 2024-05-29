# Spatial Indexes for Sanborn Atlases
This is a working repository for creating and storing geojson spatial index files. 

# How To
1. Identify an Issue you want to work on in the todo section of [the project](https://github.com/orgs/davidrumseymapcenter/projects/1)
2. Open the Issue in a new tab
![Screenshot 2024-03-26 at 2 54 23 PM](https://github.com/davidrumseymapcenter/spatial-indexes/assets/14874423/4bc5f96f-bb35-4a0e-b462-c47768162579)
3. Assign the Issue to yourself
![Screenshot 2024-03-26 at 2 55 26 PM](https://github.com/davidrumseymapcenter/spatial-indexes/assets/14874423/8773faa2-f0aa-4356-89c2-5ea801c5cd00)
4. Change the status of the project to "in progress"
5. Open [geojson.io](https://geojson.io) in a new browser window
6. Using the atlas, create a geojson file.
  - click on the little star-like icon on the page to create a new atlas plate feature. Each atlas plate will be it's own feature in the geojson file.
  - once a feature has been created, click on the "table" tab and create a new column called `plate_number`. For each plate, add the number to this column.
  - be as accurate as possible. Most plates will use streets for their boundaries which helps reduce the amount of "eye-balling" needed.
  - use a few nodes as possible by avoiding adding extra ones on straight lines.
7. Once finished working for the day, save the geojson file and upload it to github with the following file name convention: `sanborn_[city]_vol[volume number]_[year of the atlas].geojson`. the year of the atlas can be found in the Issue.
8. If the atlas needs to be continued at a later time, you can copy/paste the geojson text into geojson.io and continue working.
9. Once finished, upload the final geojson.io file and close the Issue.
