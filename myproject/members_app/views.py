from django.shortcuts import render, redirect
from django.views import View
from .utils import create_form


# import pdb; pdb.set_trace()


# Create your views here.
class MemberPage(View):
    template_name = 'input_page.html'

    def get(self, request):
        member_input = request.session.get('member_input')
        data = {
            'form': create_form(),
            'member_input': member_input
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = create_form(request_data=request.POST)

        if form.is_valid():
            request.session['member_input'] = form.cleaned_data
            return redirect('member_input')
