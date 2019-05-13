from flask import Flask

from blueprints.tree import tree_bp

app = Flask(__name__)
app.register_blueprint(tree_bp)

if __name__ == '__main__':
    app.run(debug=True)

