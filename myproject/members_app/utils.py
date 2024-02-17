from .forms import MemberForm


def create_form(request_data=None):
    if request_data:
        return MemberForm(request_data)

    return MemberForm()
