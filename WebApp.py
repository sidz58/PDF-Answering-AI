from flask import Flask, request, render_template, redirect, flash
from werkzeug.utils import secure_filename
import os
from main import cache_model, clean_text, getPrediction
import numpy

app = Flask(__name__, static_folder = 'static')
app.secret_key = "suuuper secret"
app.config['UPLOAD_FOLDER'] = 'static/'

# cache the model to save loading time
qa_model = cache_model()

# route() decorator to tell Flask what URL should trigger our function. It links the function to the URL
# render_template will be used to find the HTML file 'qa_template' HTML in the templates folder
# When we run the app it runs the qa_template.html file

@app.route('/')
def home():
    return render_template('qa_template.html')

@app.route('/', methods=['POST'])
def submit_file():

    question = request.form.get('question')

    if request.method == 'POST':
        if 'file' not in request.files: # same variable name requested in html template
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  # werkzeug method to secure filename. 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            # Extracting the answer
            answer = getPrediction(question_string = question, filename = filename, qa_model = qa_model)
            flash(answer)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            # 2 flash messages, will access as a list in html
            return redirect('/') # redirect to home page

# # Because we need to send data back and forth the frontend and backend, we use the 'POST' method, and not 'GET'
# So if we want to run our code right here, we can check if __name__ == __main__
# If we import this file to another file then __name__ == WebApp (which is the name of this python file).

if __name__ == "__main__":
    app.run(debug = True)