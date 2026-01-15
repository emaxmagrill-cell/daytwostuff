#%%
#First Line Break
#%%
#Second Line Break
#%%
#Third Line Break
#%%
# Answers to questions:
# 1. The file path is /workspaces/daytwostuff
# 2. python3 -m venv .venv && source .venv/bin/activate
# 3. No because the venv is typically located on the local machine not in the code space.
# 4. The terminal path is the same as before in the virtual environment. The terminal path is /workspaces/daytwostuff

#%%
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/MMiDS-textbook/MMiDS-textbook.github.io/refs/heads/main/utils/datasets/penguins-measurements.csv')
data.head()
#Data is the DataFrame
# %%
# 5. The extension menu is interesting because it displays a variety of extension that could be useful for projects. It also displays the extension version and creator. 
# 6. The data wrangler ui is interesting because you can visualize every variable being ran, because of the count plot of the values displays a nice visualization of the columns infomation, and the inference allows you to edit the information.

#%%
# 7. The plotly verison is 6.5.1
# 8. We use a requirements.txt file to list all the dependencies and their versions needed for a project. This allows for easy installation of the required packages. 
# %%
# Recipe: 
# 1. create a new repo
# 2. create a virtual environment
# 3. activate the virtual environment
# 4. create a requirements.txt file
# 5. install necessary packages and their versions using pip install package==version
