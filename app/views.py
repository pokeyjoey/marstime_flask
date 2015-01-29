from flask import render_template
from app import app
from app.mars.marsdate import MarsDate

active_tabs = {
    'index_active': '',
    'calculate_active': '',
    'history_active': '',
    'areogator_active': ''
}

@app.route('/zubrin_calendar')
def zubrin_calendar():
    return render_template('zubrin_calendar.html', title='Grid')

@app.route('/')
@app.route('/calendar_index')
def calendar_index():
    # get todays zubrin calendar date
    marsdate = MarsDate()
    todays_mars_calendar_date = marsdate.today()

    # set the active tab for the page navigation
    set_active_tab('index_active')
    locals().update(active_tabs)

    return render_template('calendar_index.html', **locals())

@app.route('/calendar_calculate')
def calendar_calculate():
    set_active_tab('calculate_active')
    locals().update(active_tabs)

    return render_template('calendar_calculate.html', **locals())

@app.route('/calendar_history')
def calendar_history():
    set_active_tab('history_active')
    locals().update(active_tabs)

    return render_template('calendar_history.html', **locals())

@app.route('/calendar_areogator')
def calendar_areogator():
    set_active_tab('areogator_active')
    locals().update(active_tabs)

    return render_template('calendar_areogator.html', **locals())

def set_active_tab(active_tab):
    for key in active_tabs.iterkeys():
        if key == active_tab:
            state = "active"
        else:
            state = ""

        active_tabs[key] = state

