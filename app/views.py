"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""

from flask import Module, url_for, render_template, request, redirect
from models import Todo
from forms import SearchForm
from TaskDo import ReturnWeeklyTrends
import simplejson
import urllib
views = Module(__name__, 'views')


@views.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    if request.method == 'POST':
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query="+form.search.data+"&callback=YAHOO.Finance.SymbolSuggest.ssCallback"
        page = urllib.urlopen(url)
        line = page.readlines()
        line = str(line)
        line = line[41:-3]
        json = simplejson.loads(line)
        symbol = json['ResultSet']['Result'][0]['symbol']
        
        url = "http://www.google.com/finance/info?infotype=infoquoteall&q="+symbol
        page = urllib.urlopen(url)
        line = page.readlines()
        result = str(line)

        return render_template('display.html', trends=result)
    else:
        return render_template('index.html', form=form);
    

@views.route('/display')
def display():
    trends=ReturnWeeklyTrends()
    return render_template('display.html', trends=trends)
		

@views.route('/results/')
def results():
    return render_template('results.html')

@views.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
