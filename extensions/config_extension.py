import config

def register_configs(app):
    app.config.from_object(config.BaseConfig())