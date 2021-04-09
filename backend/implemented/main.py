"""Python flask server."""
import connexion

from base import encoder

app = connexion.App(  # pylint: disable=invalid-name
    __name__, specification_dir="../base/openapi"
)
app.api_cls.jsonifier.dumps_args = dict(indent=None, separators=(",", ":"))
app.app.json_encoder = encoder.JSONEncoder
openapi_file = "openapi.yaml"  # pylint: disable=invalid-name
app.add_api(
    openapi_file, arguments={"title": "apps training RESTful API"}, pythonic_params=True,
)
flask_app = app.app  # pylint: disable=invalid-name



def main():
    """Main function to run server."""
    app.run(port=8080)


if __name__ == "__main__":
    main()
