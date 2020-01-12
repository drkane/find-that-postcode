from flask import Blueprint, current_app, abort, jsonify, make_response, request, render_template, redirect, url_for

from .utils import return_result
from findthatpostcode.controllers.areas import Area, search_areas
from findthatpostcode.db import get_db

bp = Blueprint('areas', __name__, url_prefix='/areas')


@bp.route('/search')
@bp.route('/search.<filetype>')
def area_search(filetype="json"):
    return redirect(url_for('search.search_index', q=request.values.get("q")), code=301)

@bp.route('/names.csv')
def all_names():
    pass


@bp.route('/<areacode>')
@bp.route('/<areacode>.<filetype>')
def get_area(areacode, filetype="json"):
    result = Area.get_from_es(areacode, get_db(), boundary=(filetype=='geojson'))

    if filetype == 'geojson':
        status, r = result.geoJSON()
        if status != 200:
            return abort(make_response(jsonify(message=r), status))
        return jsonify(r)

    return return_result(result, filetype, "area.html")

