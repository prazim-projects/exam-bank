import os
from django.utils.text import slugify

def exam_file_path(instance, filename):
    # Extract extension
    ext = filename.split('.')[-1]

    # Slugify course name for safety
    course_slug = slugify(instance.exam.course)

    # Build new filename: e.g., "2024-computer-science-final.pdf"
    new_filename = f"{instance.exam.year}-{course_slug}-{slugify(instance.exam.title)}.{ext}"

    # Return full path: e.g., "exams/2024/computer-science/2024-computer-science-final.pdf"
    return os.path.join(
        str(instance.exam.year),
        course_slug,
        new_filename
    )
