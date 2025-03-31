# 导入所需的Flask模块和CORS扩展
from flask import Flask, jsonify
from flask_cors import CORS

# 创建Flask应用实例
app = Flask(__name__)
# 启用CORS跨域资源共享，允许前端访问API
CORS(app)

# 定义测试路由01，返回简单的JSON消息
@app.route('/api/test01', methods=['GET'])
def test01():
    return jsonify({'message': 'Hello from Test01!'})

# 定义测试路由02，返回另一个JSON消息
@app.route('/api/test02', methods=['GET'])
def test02():
    return jsonify({'message': 'Hello from Test02!'})

# 应用入口点，启用调试模式运行服务器
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5000)