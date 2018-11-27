from flask import Flask, jsonify, request
import platform

app = Flask(__name__)


def load_model():
    """load and return the model"""
    pass

@app.route('/model', methods=["POST"])
def evaluate():
    """"Preprocessing the data and evaluate the model"""
    # TODO: data/input preprocessing
    # eg: request.files.get('file')
    # eg: request.args.get('style')
    # eg: request.form.get('model_name')

    # TODO: model evaluation
    # eg: prediction = model.eval()

    # TODO: return prediction
    # eg: return jsonify({'score': 0.95})


@app.route("/")
def main():
    system_properties = platform.uname()
    return "".join(system_properties)


if __name__ == "__main__":
    app.run( host = '0.0.0.0', threaded = False)
