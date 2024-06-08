def run():
    import subprocess

    subprocess.run(args="uvicorn apidemo.asgi:application --reload", shell=True)