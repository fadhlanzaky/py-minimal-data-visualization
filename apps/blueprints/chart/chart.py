from core.domain.charts import Chart
from core.exception import BadRequestException
from interfaces.file_interface import FileInterface
from flask import Blueprint, render_template, request

chart_bp = Blueprint(
    "chart", 
    __name__, 
    template_folder="templates", 
    static_folder="static",
    static_url_path="/chart-static")


@chart_bp.route("/")
def index():
    return render_template('index.html')


@chart_bp.route('/read_data', methods=['POST'])
def read_data():
    file = request.files.get('file', '')
    if not file:
        raise BadRequestException('No file uploaded')

    fi = FileInterface()
    filename = fi.save_file(file)
    columns =  fi.get_columns(filename)

    response = {
        'filename': filename,
        'columns': columns
    }

    return response, 200


@chart_bp.route('/generate_chart/<chart_type>', methods=['POST'])
def generate_chart(chart_type):
    param = request.form

    fi = FileInterface()
    data = fi.read_file(param.get('filename'))
    chart = Chart(data)

    chart_map = {
        'b_bc': chart.basic_bar_charts,
        'b_bp': chart.basic_box_plots,
        'b_h': chart.basic_histograms,
        'b_lc': chart.basic_line_charts,
        'b_pc': chart.basic_pie_charts,
        'b_sp': chart.basic_scatter_plots,
        'b_3lc': chart.basic_3d_line_charts
    }

    chart_method = chart_map.get(chart_type)
    if chart_method is None:
        raise BadRequestException('No method found')
    
    html_chart = chart_method(**param)
    
    response = {
        'chart': html_chart
    }
    return response, 200


@chart_bp.route('/get_col_value', methods=['GET'])
def get_col_value():
    filename = request.args.get('file', '')
    column = request.args.get('column', '')

    fi = FileInterface()
    col_vals = fi.get_columns_content(filename, column)
    return col_vals


@chart_bp.route('/delete_file', methods=['POST'])
def delete_tmp_file():
    filename = request.form.get('filename','')
    fi = FileInterface()
    fi.delete_file(filename)

    response = {
        'message': 'success'
    }

    return response, 200