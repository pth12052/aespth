from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from werkzeug.utils import secure_filename
import os
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def get_cipher(key, mode=AES.MODE_ECB, iv=None):
    key = key.encode('utf-8')
    key = key[:32].ljust(32, b'\0')  # Pad key to 32 bytes (256-bit max)
    if iv:
        return AES.new(key, mode, iv=iv)
    return AES.new(key, mode)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    file = request.files['file']
    action = request.form['action']
    key = request.form['key']
    
    if not file or not key:
        return "File và khóa là bắt buộc.", 400

    data = file.read()

    try:
        if action == 'encrypt':
            cipher = get_cipher(key)
            encrypted = cipher.encrypt(pad(data, AES.block_size))
            filename = secure_filename(file.filename) + '.enc'
            return send_file(io.BytesIO(encrypted), download_name=filename, as_attachment=True)
        
        elif action == 'decrypt':
            cipher = get_cipher(key)
            decrypted = unpad(cipher.decrypt(data), AES.block_size)
            filename = secure_filename(file.filename).replace('.enc', '')
            return send_file(io.BytesIO(decrypted), download_name=filename, as_attachment=True)
        
    except Exception as e:
        return f"Lỗi: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
