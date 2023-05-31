from app.proxies.tflow_serving_proxy import TFlowServingProxy


def classifier_proxy():
    return TFlowServingProxy()
