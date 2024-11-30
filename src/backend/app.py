# from flask import Flask
# from flask_cors import CORS
# from routes import routes
# from flask import Flask, render_template, request
# def create_app():
    
#     """
#     Create and configure the Flask application.
#     """
#     app = Flask(__name__)
#     # Enable Cross-Origin Resource Sharing (CORS) to allow communication with the frontend
#     CORS(app)

#     # Register routes from the routes blueprint
#     app.register_blueprint(routes)

#     return app


# # Initialize the app
# app = create_app()

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     # Run the Flask app
#     app.run(host="0.0.0.0", port=5000, debug=True)



import sys
import os
from flask import Flask, render_template
from flask_cors import CORS

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from routes import routes

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(routes)  # Registering the blueprint
    return app

# Initialize the app
app = create_app()

@app.route("/")
def home():
    return render_template("index.html", summarize_answer=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
