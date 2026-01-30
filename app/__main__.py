from flask import Flask, send_file, render_template_string
import requests
from io import BytesIO

app = Flask(__name__)

IMAGE_URL = "https://franco.panzani.com/_ipx/f_webp&q_80&s_1800x1192/https://backend.franco.panzani.com/app/uploads/2024/07/lasagne-classique.jpg"

@app.route('/lasagne')
def get_image():
    try:
        response = requests.get(IMAGE_URL, timeout=10)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', 'image/jpeg')
        
        return send_file(
            BytesIO(response.content),
            mimetype=content_type
        )
    except Exception as e:
        return f"Erreur lors de la récupération de l'image: {str(e)}", 500

if __name__ == '__main__':
    print(f"🖼️  Image source: {IMAGE_URL}")
    app.run(debug=True, host='0.0.0.0', port=8180)