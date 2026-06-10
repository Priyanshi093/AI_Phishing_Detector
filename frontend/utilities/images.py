import base64

def get_base64_image(path: str) -> str:
    """Converting a local image file to a base64-encoded string."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def load_all_images() -> dict:
    """
    Loading all app icons used across pages.
    Returns a dict keyed by short names.
    """
    return {
        "logo":  get_base64_image("frontend/icons/phishing.png"),
        "img1":  get_base64_image("frontend/icons/txt-file.png"),
        "img2":  get_base64_image("frontend/icons/monitor.png"),
        "img3":  get_base64_image("frontend/icons/performance.png"),
        "img4":  get_base64_image("frontend/icons/secure.png"),
        "img5":  get_base64_image("frontend/icons/secure_browse.png"),
    }