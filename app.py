from flask import Flask, request
import g4f

app = Flask(__name__)

#@app.route('/transfer_data', methods=['POST'])
#def transfer_data():
#    if request.method == "POST":
#      query = request.json['query']  # 取得POST傳遞的JSON資訊
#      g4f.debug.logging = False
#      g4f.debug.version_check = False
#      response = g4f.ChatCompletion.create(
#        model = g4f.models.gpt_4,
#        messages = [{"role": "user", "content": query}],
#      )
#      return response
#    else:
#      return "Unsupported Method"
#
#if __name__ == '__main__':
#    app.run()

@app.route('/',methods=["GET"])
def query():
    return "success"
