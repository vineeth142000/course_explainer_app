# Videos Tab — Implementation Tasks

## Goal
Add a "Videos" navigation tab that embeds YouTube teaching videos, grouped by course.

## Plan

### Architecture
- Add a `videos` field to the `Course` model — a list of dicts with `title` and `youtube_id`
- Add a new route `GET /videos` in `app.py`
- Add a `videos()` view function in `views.py` that passes all courses to the template
- Create `src/templates/videos.html` that renders YouTube `<iframe>` embeds grouped by course
- Add a "Videos" link to the nav in `layout.html`
- Add unit tests for the `/videos` route

### YouTube embed format
Each video stored as `{ "title": "...", "youtube_id": "XXXXXXXXXXX" }`.  
Embed URL: `https://www.youtube.com/embed/{youtube_id}`

---

## Tasks

- [x] **1. Update `Course` model** (`src/models.py`)
  - Add `videos` parameter (default `[]`) to `Course.__init__`
  - Add sample YouTube video data to each course in the `courses` list

- [x] **2. Add `/videos` route** (`src/app.py`)
  - Register `GET /videos` → `videos` view function

- [x] **3. Add `videos` view function** (`src/views.py`)
  - Import and define `videos()` — passes `courses` to `videos.html`

- [x] **4. Create `videos.html` template** (`src/templates/videos.html`)
  - Extends `layout.html`
  - Groups embeds by course (heading per course)
  - Renders YouTube `<iframe>` for each video with responsive sizing
  - Shows a message if no videos are available for a course

- [x] **5. Update nav in `layout.html`**
  - Add `<li><a href="{{ url_for('videos') }}">Videos</a></li>` to `.main-nav`

- [x] **6. Add unit tests** (`tests/test_app.py`)
  - `test_videos_page` — GET `/videos` returns 200 and contains "Videos"
  - `test_videos_contains_course_names` — page lists course titles
  - `test_videos_contains_youtube_embed` — page contains `youtube.com/embed`

- [x] **7. Run tests and verify all pass**
  ```
  python -m unittest discover -s tests
  ```
