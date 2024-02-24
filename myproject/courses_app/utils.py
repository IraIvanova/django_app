from .forms import CourseForm


def create_form(request_data=None):
    if request_data:
        return CourseForm(request_data)

    return CourseForm()
