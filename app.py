from flask import Flask, request, jsonify
import google.generativeai as genai
import os
import json
 
 
genai.configure(api_key="AIzaSyDuYut8WDv0ywkcuyjqdhYn7ENSNnvtlyM")  
 
app = Flask(__name__)
 
 
@app.route('/query_llm', methods=['POST'])
def query_llm():
    try:
        data = request.get_json()
        print(data)
        question = data.get("question")
        data_context = data.get("data_context")        
        prompt = f"Based on the following data: {data_context}, answer this question: {question}. Just give the name alone."
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        answer = response.text if response else "No response received."
        return jsonify({"answer": answer})
   
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)