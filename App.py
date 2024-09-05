from datetime import datetime

from flask import Flask,jsonify,request, render_template
from Model import db,Users,Baselines

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

# 路由函数，用于获取所有用户数据
@app.route('/users', methods=['GET'])
def get_users():
    with app.app_context():  # 确保在应用上下文中运行
        users = Users.query.all()
        return jsonify([user.to_dict() for user in users])

@app.route('/baseline', methods=['POST'])
def create_baseline():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    baseline_name = data.get('baseline_name')
    baseline_status = data.get('baseline_status')
    owner = data.get('owner')
    timestamp = datetime.utcnow()
    if not baseline_name or not baseline_status or not owner:
        return jsonify({'error': 'Missing required fields'}), 400
    new_baseline = Baselines(
        baseline_name=baseline_name,
        baseline_status=baseline_status,
        owner=owner,
        timestamp=timestamp
    )
    db.session.add(new_baseline)
    db.session.commit()
    return jsonify(new_baseline.to_dict()), 201


@app.route('/baselines', methods=['GET'])
def get_baseline():
    baselines = Baselines.query.all()
    return jsonify([baseline.to_dict() for baseline in baselines])

if __name__ == '__main__':
    app.run()