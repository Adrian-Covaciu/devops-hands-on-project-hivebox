from prometheus_flask_exporter import PrometheusMetrics
from blueprints.version import application_version

def init_metrics(app):
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version=application_version)
