# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8 as dependencies

RUN apt-get update

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Install pip requirements
COPY requirements/base.txt .
COPY requirements/test.txt .
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:/template-django"
RUN python -m pip install --no-cache-dir -r test.txt

# --- Release with slim api ----
FROM python:3.8-slim-buster AS release

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:/template-django"

WORKDIR /app
COPY --from=dependencies /venv /venv
COPY /app /app

EXPOSE 8000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi", "--reload"]
