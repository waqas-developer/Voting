from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render

# Create your views here.


class GetSlip(View):
    template_name = "votingBooth/slip.html"

    def get(self, request):
        cnic = request.GET.get("cnic")
        voter_name = request.GET.get("voter_name", "")
        guardian = request.GET.get("guardian", "")
        block_code = request.GET.get("block_code", "")
        voter_number = request.GET.get("series_number", "")
        pp = request.GET.get("provincial_constituency_number", "")
        na = request.GET.get("na", "")
        booth_number = request.GET.get("pollingStation_name", "")

        context = {
            "voter_name": voter_name,
            "guardian": guardian,
            "block_code": block_code,
            "voter_number": voter_number,
            "pp": pp,
            "na": na,
            "booth_number": booth_number,
        }
        print(context)

        return render(request, self.template_name, context)
