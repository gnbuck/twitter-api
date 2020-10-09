from flask_restx import Namespace, Resource, fields
from flask import abort

from app.db import tweet_repository

api = Namespace('tweets')

tweet_model = api.model("Tweet", {
    "id": fields.String,
    "text": fields.String,
    "created_at": fields.String,
})

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):

    @api.marshal_with(tweet_model)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404, 'Tweet not found')
        else:
            return tweet
