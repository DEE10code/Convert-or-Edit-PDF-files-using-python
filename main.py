import pikepdf
from pikepdf import Pdf, PdfImage
import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
       # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))  
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)





"""

file = request.files['file']
        pdf = pikepdf.Pdf.open(file)
        pdf.save("Replace.pdf")
        # response = make_response(send_file(file, download_name="project_pdf", mimetype='application/pdf', as_attachment=True))
        # response = make_response(send_file(io.BytesIO(file.getbuffer())))
        # response.headers.set('Access-Control-Allow-Origin', '*')
        return f'Uploaded: {file.filename}'

"""