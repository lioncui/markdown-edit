from app import app
from flask import render_template
from flask import request
from flask import url_for
from flask import Markup
from flask import jsonify
from markdown import markdown

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/convert_md', methods = ['POST'])
def convert_md():
    html_text = request.form.get('html_text', None)
    if html_text != None:
        md_text = markdown(html_text, extensions = ['fenced_code', 'tables'])
        md_text = Markup(md_text)
        return jsonify(result = md_text)
    return jsonify(result = "None")

@app.errorhandler(404)  
def not_found(e):  
    return render_template('404.html'), 404