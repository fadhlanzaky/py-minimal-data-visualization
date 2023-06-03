import pandas as pd
import plotly.express as px
import plotly.io as pi
import os
from funcs.controller.controller import TMP_DIR

def read_file(filename):
    # Define filepath
    file_path = os.path.join(TMP_DIR, filename+'.csv')

    # Read file if exists
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        columns = df.columns
        return df, columns
    else:
        raise Exception('File not found.')
    
def basic_scatter_plots(filename, column_index_x, column_index_y):
    # Get dataframe and its columns
    df, columns = read_file(filename)

    # Get data X and Y
    data_x = columns[column_index_x]
    data_y = columns[column_index_y]

    # Create chart and transform it to html
    chart = px.scatter(x=df[data_x], y=df[data_y])
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result

def basic_box_plots(filename, column_index_x, column_index_y, column, value):
    # Get dataframe and its columns
    df, columns = read_file(filename)

    # Get data X and Y
    data_x = columns[column_index_x]
    data_y = columns[column_index_y]

    # Filter dataframe
    df = df.loc[df[columns[column]] == value]

    # Create chart and trasform it to html
    chart = px.box(x=df[data_x], y=df[data_y])
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result

def basic_line_charts(filename, column_index_x, column_index_y, column, value):
    # Get datarframe and its columns
    df, columns = read_file(filename)

    # Get data X and Y
    data_x = columns[column_index_x]
    data_y = columns[column_index_y]

    # Filter dataframe
    df = df.loc[df[columns[column]] == value]

    # Create chart and transform it to html
    chart = px.line(df, x=data_x, y=data_y)
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result

def basic_bar_charts(filename, column_index_x, column_index_y, column):
    # Get dataframe and its columns
    df, columns = read_file(filename)

    # Get data X and Y
    data_x = columns[column_index_x]
    data_y = columns[column_index_y]

    # Y datatype recondition
    try:
        df[data_y].astype(float)
    except:
        raise Exception("Make sure Y axis is numerical")

    # Create chart and transform it to html
    chart = px.bar(df, x=data_x, y=data_y, color=columns[column])
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result

def basic_pie_charts(filename, column_index_x, column_index_y):
    # Get dataframe and its columns
    df, columns = read_file(filename)

    # Get data X and Y
    data_x = columns[column_index_x]
    data_y = columns[column_index_y]

    # X datatype recondition
    try:
        df[data_x].astype(float)
    except:
        raise Exception("Make sure the data you want to show is numerical")
    
    # Changing the name of the category to 'Other' if the value below average
    df.loc[df[data_x] < df[data_x].mean(), data_y] = 'Other'

    # Create chart and transform it to html
    chart = px.pie(df, values=data_x, names=data_y)
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result

def basic_histograms(filename, column_index_x):
    # Get dataframe and its columns
    df, columns = read_file(filename)

    # Get X data
    data_x = columns[column_index_x]

    # Create chart and transform it to html
    chart = px.histogram(df, x=df[data_x])
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result

def basic_3d_line_charts(filename, column_index_x, column_index_y, column_index_z, column, value):
    # Get dataframe and its columns
    df, columns = read_file(filename)

    # Get data X, Y, and Z
    data_x = columns[column_index_x]
    data_y = columns[column_index_y]
    data_z = columns[column_index_z]

    # Dataframe filter
    df    = df.loc[df[columns[column]] == value]

    # Create chart and transform it to html
    chart = px.line_3d(df, x=data_x, y=data_y, z=data_z)
    html_chart = pi.to_html(chart)

    result = {"message": html_chart}
    return result