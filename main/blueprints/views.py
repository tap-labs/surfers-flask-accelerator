from flask import render_template, request, redirect, abort
from flask import current_app as app
from . import bp


@bp.route('/', methods=["GET"])
def home():
    app.logger.info("Accessing home page")
    _color = app.config['COLOR']
    return render_template('home.html', color=_color)


## Jinja Functions 
@bp.context_processor
def utilities():
    def color_code(color):
        match color:
            case 'red':
                _code = '#FF0000'
            case 'blue':
                _code = '#0000FF'
            case 'green':
                _code = '#00FF00'
            case 'yellow':
                _code = '#FFFF00'
            case _:
                _code = '#800080'

        return _code

    return dict(color_code=color_code)
