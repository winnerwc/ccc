from datetime import datetime

from flask import Flask,jsonify,request, render_template
from Model import db,Users,Baselines,Project
from sqlalchemy.sql import text
import re

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


def sanitize_table_name(table_name):
    # 只允许字母、数字和下划线
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '', table_name)
    return sanitized

@app.route('/projects/<project_name>', methods=['GET'])
def get_projects(project_name):
    # 清理并验证表名
    sanitized_project_name = sanitize_table_name(project_name)

    table_name = f'{sanitized_project_name.lower()}'
    print(table_name)
    # 构建查询语句，并使用text()函数显式声明
    query = text(f'SELECT * FROM {table_name}')

    try:
        # 执行查询
        result = db.session.execute(query)

        # 将查询结果转换为列表
        projects = []
        for row in result:
            # 将每一行转换为字典并追加到列表中
            print(row)
            row_dict = dict(row._mapping.items())
            projects.append(row_dict)

        return jsonify(projects), 200
        # projects = db.session.execute(query)
        # # 将查询结果转换为列表
        # #projects = [dict(row) for row in result]
        # print([dict(row) for row in projects])
        # return jsonify([project.to_dict() for project in projects])
    except Exception as e:
        return jsonify({'error': f'Failed to fetch data from {table_name}: {str(e)}'}), 500

if __name__ == '__main__':
    app.run()