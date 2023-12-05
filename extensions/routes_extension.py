from apps.blueprints.chart import chart

def register_routes(app):

    app.register_blueprint(chart.chart_bp)