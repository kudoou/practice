from flask import Flask, render_template, request, jsonify #untuk mencari file html kita secara spesifik

app = Flask(__name__)

## Setiap URL memiliki nama fungsi yang sama,
## Alama-alamat pada route('/'), dll. harus tidak boleh sama.
@app.route('/')
def home():
    return render_template('index.html')

# fungsi ini untuk memisahkan pemetaan 
@app.route('/mypage')
def homepage():
    return 'This is Mypage'

# membuat routing get untuk requesting data 
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({
        'result':'success', 
        'msg': 'GET this request!'
    })

# membuat routing POST Digunakan saat request create, update, atau delete data
@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({
        'result':'success', 
        'msg': 'This request is POST!'
    })


if __name__ == '__main__' :
    app.run('0.0.0.0',port=5000, debug=True)
    
