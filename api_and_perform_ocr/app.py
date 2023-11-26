from flask import Flask, request, jsonify, render_template
from perform_ocr import perform_ocr
import io
 
app = Flask(__name__)
 
@app.route('/receive_image', methods=['POST'])
def receive_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No image received'})
 
    file = request.files['file']
 
    if file.filename == '':
        return jsonify({'message': 'No image selected'})
 
    try:
        # Read image data from the request
        image_data = file.read()
 
        # Call the perform_ocr function with image data
        result = perform_ocr(image_data)
 
        # Render an HTML template with the OCR results
        return render_template('ocr_result.html', file_name=file.filename, ocr_result=result)
 
    except Exception as e:
        return jsonify({'message': f'Error processing image: {str(e)}'})
 
if __name__ == '__main__':
    app.run(debug=True)