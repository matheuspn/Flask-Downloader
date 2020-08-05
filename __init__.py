from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    send_file,
    session,
)

from ydl import get_media, fetch_name
from zipper import zipping

app = Flask(__name__)
app.secret_key = "supposed to be a secret"


@app.route("/return-file/")
def return_file():

    num_choice = session.get("choice")
    filename = session.get("filename")

    if num_choice == 1:
        filename_formatted = filename + ".mp3"
        location = "media/Audio downloads/{}.mp3".format(session.get("id"))

    if num_choice == 2:
        filename_formatted = filename + ".mp4"
        location = "media/Video downloads/{}.mp4".format(session.get("id"))

    if num_choice == 3 or num_choice == 4:
        filename_formatted = filename + ".zip"
        location = "media/{}.zip".format(session.get("id"))

    return send_file(
        location, attachment_filename=filename_formatted, as_attachment=True
    )


@app.route("/", methods=["GET", "POST"])
def index():
    """
	Displaying homepage
	"""

    title = "YDL | YouTube Downloader"

    if request.method == "POST":

        attempted_url = request.form["url"]
        attempted_choice = int(request.form["submit"])
        title = [attempted_url, attempted_choice]
        if attempted_url != "":

            result_id = get_media(attempted_url, attempted_choice)
            session["url"] = attempted_url
            session["id"] = result_id
            session["choice"] = attempted_choice
            filename = fetch_name(attempted_url)
            session["filename"] = filename
            return redirect(url_for("return_file"))
        else:
            return render_template(
                "index.html", title="YDL | URL shouldn't be empty"
            )

    return render_template("index.html", title=title)


@app.errorhandler(404)
def page_not_found(error):
    """
	for anyone trying different links or searching for images within the server
    """
    return (
        render_template(
            "error_template.html",
            title="404 bud",
            message="Trying to access a non exist page. ",
            subline="Back to",
            
        ),
        404,
    )


@app.errorhandler(400)
def bad_request(error):
    """
	For handling situations where the server doesn't know what to do with the browser's request
	"""
    return (
        render_template(
            "error_template.html",
            title="Aaaah ...",
            message="나는 이해하지 못한다.",
            subline="Yeah, the server couldn't understand what you asked for, Sorry",
            
        ),
        400,
    )

@app.errorhandler(500)
def invalid_url(error):
    """
	for anyone trying different links or searching for images within the server
    """
    return (
        render_template(
            "error_template.html",
            title="YDL | URL must be valid",
            message="Time to make the chimi-fuckin'-changas. ",
            subline="500, not there",
            
        ),
        500,
    )


if __name__ == "__main__":

    app.run()
