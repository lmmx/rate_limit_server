from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,  # Uses the remote address for rate limiting
    default_limits=["5 per minute"],  # Limit: 5 requests per minute
)


@app.route("/data")
@limiter.limit("3 per minute")  # Custom limit for this endpoint
def index():
    return "This is a rate-limited response."


if __name__ == "__main__":
    app.run(debug=True)
