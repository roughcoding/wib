from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)


@app.route('/', methods=['POST'])
async def test(request):
    if request.json['greet_me']:
        return json({'hello': 'world'})
    else:
        return json({})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8100, workers=1)
