from flask import Flask, render_template, request
from funcs.charts.charts import (basic_3d_line_charts, 
                                 basic_bar_charts, 
                                 basic_box_plots, 
                                 basic_histograms, 
                                 basic_line_charts, 
                                 basic_pie_charts, 
                                 basic_scatter_plots)
from funcs.controller.controller import delete_file, get_value, main

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

@app.errorhandler(413)
def request_entity_too_large(error):
    print(error)
    return {'error': str(error)}, 413

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/read_data', methods=['POST'])
def read_data():
    file = request.files.get('file', '')
    if not file:
        return {'error': 'No file uploaded'}, 500
    return main(file)
    
@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    data = request.form
    charts = data.get('charts', '')

    try:
        # Scatter Plot
        if charts == 'b_sp':
            return basic_scatter_plots(data['filename'], int(data['x']), int(data['y']))
        # Box Plot
        elif charts == 'b_bp':
            return basic_box_plots(data['filename'], int(data['x']), int(data['y']), int(data['query_col']), data['query_val'])
        # Line Chart
        elif charts == 'b_lc':
            return basic_line_charts(data['filename'], int(data['x']), int(data['y']), int(data['query_col']), data['query_val'])
        # Bar Chart
        elif charts == 'b_bc':
            return basic_bar_charts(data['filename'], int(data['x']), int(data['y']), int(data['query_col']))
        # Pie Chart
        elif charts == 'b_pc':
            return basic_pie_charts(data['filename'], int(data['x']), int(data['y']))
        # Histogram
        elif charts == 'b_h':
            return basic_histograms(data['filename'], int(data['x']))
        # 3d Line Chart
        elif charts == 'b_3lc':
            return basic_3d_line_charts(data['filename'], int(data['x']), int(data['y']), int(data['z']), int(data['query_col']), data['query_val'])
    except Exception as e:
        return {'message': str(e)}, 500

@app.route('/get_col_value', methods=['GET'])
def get_col_value():
    filename = request.args.get('file', '')
    column_index = request.args.get('column_index', 0)
    return get_value(filename, int(column_index))

@app.route('/delete_file', methods=['POST'])
def delete_tmp_file():
    filename = request.form.get('filename','')
    return delete_file(filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)