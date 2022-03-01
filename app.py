from flask import Flask, render_template, request
import os
import cost_calculator

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def landing_page():
    output = render_template('landing_page.html')
    return output


@app.route('/aboutus')
def about_us():
    output = render_template('about_us.html')
    return output

@app.route('/centralintelligenceserviceccp')
def attention_citizen():
    output = render_template('attention_citizen.html')
    return output

@app.route('/bookings', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        adults = int(request.form['num_adults'])
        children = int(request.form['num_children'])
        total = cost_calculator.total_cost(adults, children)
        return render_template('result.html',
                               adults=adults,
                               children=children,
                               total=total)
    return render_template('form.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run()
