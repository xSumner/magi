from flask import Flask, request

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert():
    info = request.json
    name = info['name']
    age = info['age']
    age_after_10_years = age + 10
    msg = f'此人名叫：{name}，10年后，此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}

if __name__ == '__main__':
    app.run(debug=True)