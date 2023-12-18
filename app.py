from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_google():
    if request.method == 'POST':
        keyword = request.form.get('keyword', '')
        max_results = request.form.get('max_results', '5')
        
        if max_results.isdigit():
            max_results = int(max_results)
            results = list(search(keyword, num=max_results, stop=max_results, pause=2))
            return render_template('index.html', keyword=keyword, results=results, max_results=max_results)

    return render_template('index.html')  # Return default template if form not submitted properly

if __name__ == '__main__':
    app.run(debug=True)
