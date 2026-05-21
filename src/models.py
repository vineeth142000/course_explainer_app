class Course:
    def __init__(self, title, description, instructor, duration, topics=None, videos=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics or []
        self.videos = videos or []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course(
        "Introduction to Python",
        "Learn the basics of Python programming.",
        "John Doe",
        "4 weeks",
        ["Variables and Data Types", "Control Flow", "Functions", "Modules"],
        [
            {"title": "Learn Python – Full Course for Beginners (freeCodeCamp)", "youtube_id": "rfscVS0vtbw"},
            {"title": "Python for Beginners – Full Course (freeCodeCamp)", "youtube_id": "eWRfhZUzrAc"},
        ],
    ),
    Course(
        "Web Development with Flask",
        "Build web applications using Flask.",
        "Jane Smith",
        "6 weeks",
        ["Flask Basics", "Routing", "Templates", "Forms", "Databases"],
        [
            {"title": "Learn Flask for Python – Full Tutorial (freeCodeCamp)", "youtube_id": "Z1RJmh_OqeA"},
            {"title": "Python Flask Tutorial for Beginners – Full Course", "youtube_id": "3mwFC4SHY-Y"},
        ],
    ),
    Course(
        "Data Science Fundamentals",
        "An introduction to data science concepts and tools.",
        "Alice Johnson",
        "8 weeks",
        ["NumPy", "Pandas", "Matplotlib", "Machine Learning Basics"],
        [
            {"title": "Learn Data Science – Full Course for Beginners (freeCodeCamp)", "youtube_id": "ua-CiDNNj30"},
            {"title": "Data Science Full Course – 12 Hours (Edureka)", "youtube_id": "xiEC5oFsq2s"},
        ],
    ),
]