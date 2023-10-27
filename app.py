from flask import Flask, render_template, request, jsonify
import openai  # Install using: pip install openai

app = Flask(__name__)

# Add your OpenAI GPT-3 API key here
api_key = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data=request.json
    keyword = data.get('keyword')
    language = data.get('language')  # Assuming a dropdown for language selection
    

    # Call the OpenAI API to convert the keyword to code in the selected language
    code = generate_code(keyword, language)

    return jsonify({'code': code})

def generate_code(keyword, language):
    
    
    # Use the OpenAI GPT-3 API to generate code based on the keyword and language
    openai.api_key = api_key

    # You need to create an appropriate prompt for code generation
    prompt = f"Convert this code '{keyword}' to {language} code:"

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model
            messages=[
                
                  {"role": "user", "content": prompt}]
        )
    print(keyword)
    print(language)
    print(response)
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)