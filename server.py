from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    routes = {
            'Greeting': '/calculator/greeting',
            'Add': '/calculator/add',
            'Subtract': '/calculator/subtract'
            # Add more routes as needed
        }
    # Generate HTML with clickable links
    html = '<h1>Welcome to the Home Page</h1>'
    html += '<h2>Links to Other Pages:</h2>'
    html += '<ul>'
    
    for title, url in routes.items():
        html += f'<li><a href="{url}">{title}</a></li>'
    
    html += '</ul>'
    
    return html

@app.route("/calculator/greeting")
def greeting():
    return 'hemlu krits'

@app.route("/calculator/add")
def add():
    return 'one plus one'

@app.route("/calculator/subtract")
def subtract():
    return str(1-1)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
