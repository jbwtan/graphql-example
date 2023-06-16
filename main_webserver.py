from flask import Flask
from graphql_server.flask import GraphQLView

from main_local import schema, query

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))

if __name__ == '__main__':
    print(f"Query to execute: {query}")
    app.run()