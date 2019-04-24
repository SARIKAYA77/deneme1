from flask import Flask
import task


app = Flask(__name__)

@app.route('/')
def anket():
    result = task.startTask()

    return result

