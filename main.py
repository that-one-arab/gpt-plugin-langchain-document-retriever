from dotenv import load_dotenv

load_dotenv()

import os
import quart
import quart_cors
from quart import request, jsonify
from quart.utils import run_sync
from lib.vectordb.query import query_docs

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

IS_PRODUCTION = os.getenv('PRODUCTION') == "True"
PRODUCTION_URL = os.getenv('PRODUCTION_URL')
PRODUCTION_EMAIL = os.getenv('PRODUCTION_CONTACT_EMAIL')

def get_answer_template():
    """
    Defines the shape of the plugin's answer. This is the answer shape that the plugin will return
    """
    return """
[DEFINE YOUR ANSWER SHAPE HERE]
"""

@app.get('/hello')
async def hello():
    return jsonify(message="Hello, World!")

@app.post("/api/query")
async def query():
    request = await quart.request.get_json(force=True)
    query: str = request['query']

    def sync_processor():
         return query_docs(query)

    response = await run_sync(sync_processor)()

    template = get_answer_template()

    return jsonify({
        "template": template,
        "hadiths": response
    })

@app.get("/logo.png")
async def plugin_logo():
    filename = './static/openai/logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("./static/openai/.well-known/ai-plugin.json") as f:
        text = f.read()
        if IS_PRODUCTION:
            text = text.replace("http://localhost:5000", PRODUCTION_URL)
            text = text.replace("test@test.com", PRODUCTION_EMAIL)
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    with open("./static/openai/openapi.yaml") as f:
        text = f.read()
        if IS_PRODUCTION:
            text = text.replace("http://localhost:5000", PRODUCTION_URL)
        return quart.Response(text, mimetype="text/yaml")

@app.get("/legal_info")
async def legal_info():
    host = request.headers['Host']
    with open("./static/html/legal_info.html") as f:
        html = f.read()
        return quart.Response(html)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)