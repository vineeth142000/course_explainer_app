# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the app:**
```
python src/app.py
```
App runs at `http://127.0.0.1:5001`. Must be run from the project root so that Flask resolves `src/templates/` correctly. Port 5000 is avoided because macOS AirPlay Receiver occupies it.

**Run tests:**
```
python -m unittest discover -s tests
```

**Run a single test:**
```
python -m unittest tests.test_app.AppTestCase.test_index
```

**Install dependencies:**
```
uv pip install -r requirements.txt
```

## Architecture

This is a minimal Flask app with a flat MVC-style structure inside `src/`:

- [src/app.py](src/app.py) — Flask entry point. Registers two routes: `GET /` → `index`, `GET /course/<course_id>` → `course`.
- [src/views.py](src/views.py) — Route handler functions imported directly into `app.py` (not a Blueprint).
- [src/models.py](src/models.py) — `Course` class and a hardcoded `courses` list (no database). Views don't yet use this data — connecting `models.courses` to `views.py` and passing course objects to templates is the main pending work.
- [src/templates/](src/templates/) — Jinja2 templates. `layout.html` is the base layout (header/nav/footer). `course.html` correctly extends it with `{% extends 'layout.html' %}`. `index.html` currently misuses `{% include 'layout.html' %}` instead of extending it — this causes duplicate HTML structure.

**Known template inconsistency:** `course.html` expects a `course` object with `.title`, `.description`, `.instructor`, `.duration`, and `.topics` attributes, but `views.py` only passes `course_id`. The template will error until `views.py` looks up the course from `models.courses` and passes it to `render_template`.

## Add Unit Tests

- whenever you add any changes add unit tests and run and make sure the tests passes.