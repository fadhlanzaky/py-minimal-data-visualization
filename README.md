# py-minimal-data-visualization

This was my first attempt at data visualization using plotly.
I prepared 7 different chart utilities (Scatter Plots, Box Plots, Line Charts, 3D Line Charts, Bar Charts, Pie Charts, and Histogram).

to use it, just install all the required libs
```sh
  pip install -r requirements.txt
 ```
 
 and start the application
 ```sh
  flask run
 ```
 
 This app reads data from the uploaded csv file, store it in tmp folder, and delete it after. All the csv files that I've tried were sourced from [kaggle datasets](https://www.kaggle.com/datasets), I included some of the files in datasets folder.