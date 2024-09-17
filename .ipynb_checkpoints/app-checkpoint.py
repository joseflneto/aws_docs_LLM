from utils import get_LLM
from flask import Flask, jsonify, request


app = Flask(__name__)
print("Setting LLM...")
llm = get_LLM()
print("LLM ready!")

@app.route('/LLM', methods=['POST'])
def LLM_function():
    data = request.get_json()
    query = data.get('query')
    result = llm({"query": query})
    
    response = {
            'answer': result['result'],
            'source_documents': [doc.metadata['source'] for doc in result['source_documents']]
       }
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



