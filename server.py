from flask import Flask, request, send_file
import subprocess
from generator import generate_manim_code

app = Flask(__name__)

@app.route("/render")
def render_animation():
    topic = request.args.get("topic", "hello")

    # Generate Manim code
    code = generate_manim_code(topic)

    # Write code to scene.py
    with open("scene.py", "w") as f:
        f.write(code)

    # Render with Manim
    subprocess.run(
        ["python", "-m", "manim", "-pql", "scene.py", "AutoScene"],
        check=True
    )

    video_path = "media/videos/scene/480p15/AutoScene.mp4"
    return send_file(video_path, mimetype="video/mp4")


if __name__ == "__main__":
    app.run(port=5000)
