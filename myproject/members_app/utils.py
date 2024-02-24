from .forms import CreateMemberForm


def create_member_form(request_data=None):
    if request_data:
        return CreateMemberForm(request_data)

    return CreateMemberForm()
