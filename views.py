from pyramid.view import view_config
from models import *


@view_config(renderer="templates/index.pt")
def index_view(request):
    return {}

@view_config(renderer="templates/pc.pt", name="pc")
def pc_view(request):
    return {"pcs": PC.select()}