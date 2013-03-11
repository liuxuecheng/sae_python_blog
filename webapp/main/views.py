from flask import Blueprint, render_template
from domain import get_version

main_page = Blueprint('main_page', __name__)

@main_page.route('/')
def index():
    version = get_version()
    return render_template('/layout/main.html',
        version=version,
    )
