from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    data = request.form
    return render_template('resume_template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
