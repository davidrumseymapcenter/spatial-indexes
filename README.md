# Spatial Indexes for Insurance Atlases
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

# Aligning Index Points
1. If you have not done so already, you will need to install python and Visual Studio Code. You can download the python installer from [this page](https://www.python.org/downloads/) and the Visual Studio Code installer from [this page](https://code.visualstudio.com/Download).
2. Crete a new folder on your computer named _spatial-index-alignment_.
3. Download _alignment-script.py_ and move it to your new folder.
4. Open your _spatial-index-alignment_ folder in Visual Studio Code. [^1]
5. Open the Terminal below the script (View > Terminal) and set up a virtual environment: [^2]\
`python -m venv .index-alignment-venv`
7. Open a **new** Terminal (Terminal > New Terminal) and use `pip install` to install the following packages: [^3]
  - `pip install geopandas`
  - `pip install scipy`
9. Download the spatial index .geojson file you want to align and move it to your _spatial-index-alignment_ folder.
10. Open _alignment-script.py_ in VS Code and replace *input_file_name_here.geojson* with the name of your spatial index file.
12. Replace *output_file_name_here.geojson* to name the file that will be created. Follow the convention `aligned_[atlas]_[city]_vol[volume number]_[year of the atlas].geojson`
13. Run the script and upload the resulting file to the spatial-indexes repository.

[^1]:If you haven't already, you may want to install the VS Code python extension. Upon opening the script for the first time, a popup may appear asking if you would like to install the extension. Alternatively, you can install it from the Extensions Sidebar Tab (Shift+Command+X). This is not required to run the script.
[^2]:If you get "command not found" errors using the `python` and `pip` commands, try using `python3` and `pip3` instead. This will depend on your operating system, python installation version, etc. More info can be found [here](https://www.reddit.com/r/learnpython/comments/mf7t0n/why_python3_in_command_prompt_vs_python/).
[^3]:This script requires four total packages to run properly: geopandas, shapely, numpy, and scipy. You won't need to individually install shapely and numpy as they are dependencies of geopandas and are included in your geopandas installation.
<!-- [^4]:Note about setting equivalent python versions in VS Code -->