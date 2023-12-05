import plotly.express as px
import plotly.io as pi

from core.exception import BadRequestException
from core.utilities import adjust_kwargs

class Chart(object):

    def __init__(self, data) -> None:
        self.data = data

    @adjust_kwargs
    def basic_scatter_plots(self, column_x, column_y):
        # Get data X and Y
        data_x = self.data[column_x]
        data_y = self.data[column_y]

        # Create chart and transform it to html
        chart = px.scatter(x=data_x, y=data_y)
        html_chart = pi.to_html(chart)

        return html_chart
    
    @adjust_kwargs
    def basic_box_plots(self, column_x, column_y, query_col, query_val):
        # Filter dataframe
        filtered_df = self.data.loc[self.data[query_col].astype(str) == query_val]

        # Create chart and trasform it to html
        chart = px.box(x=filtered_df[column_x], y=filtered_df[column_y])
        html_chart = pi.to_html(chart)

        return html_chart

    @adjust_kwargs
    def basic_line_charts(self, column_x, column_y, query_col, query_val):
        # Filter dataframe
        filtered_df = self.data.loc[self.data[query_col] == query_val]

        # Create chart and transform it to html
        chart = px.line(filtered_df, x=column_x, y=column_y)
        html_chart = pi.to_html(chart)

        return html_chart
    
    @adjust_kwargs
    def basic_bar_charts(self, column_x, column_y, query_col):
        # Y datatype recondition
        try:
            self.data[column_y].astype(float)
        except:
            raise BadRequestException("Make sure Y axis is numerical")

        # Create chart and transform it to html
        chart = px.bar(self.data, x=column_x, y=column_y, color=query_col)
        html_chart = pi.to_html(chart)

        return html_chart

    @adjust_kwargs
    def basic_pie_charts(self, column_x, column_y):
        # X datatype recondition
        try:
            self.data[column_x].astype(float)
        except:
            raise BadRequestException("Make sure the data you want to show is numerical")
        
        # Changing the name of the category to 'Other' if the value below average
        self.data.loc[self.data[column_x] < self.data[column_x].mean(), column_y] = 'Other'

        # Create chart and transform it to html
        chart = px.pie(self.data, values=column_x, names=column_y)
        html_chart = pi.to_html(chart)

        return html_chart

    @adjust_kwargs
    def basic_histograms(self, column_x):
        # Create chart and transform it to html
        chart = px.histogram(self.data, x=self.data[column_x])
        html_chart = pi.to_html(chart)

        return html_chart

    @adjust_kwargs
    def basic_3d_line_charts(self, column_x, column_y, column_z, query_col, query_val):
        # Dataframe filter
        filtered_df = self.data.loc[self.data[query_col] == query_val]

        # Create chart and transform it to html
        chart = px.line_3d(filtered_df, x=column_x, y=column_y, z=column_z)
        html_chart = pi.to_html(chart)

        return html_chart