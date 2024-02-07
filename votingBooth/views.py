from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render
from .utils import GenerateGPTResponse,getVotterandGardian
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
        na = request.GET.get("constituency_number", "")
        booth_number = request.GET.get("pollingStation_name", "")
        prompt = f"convert my voter_name which is  {voter_name} and guardian name which is  {guardian} in urdu writing and return python dictionary format like" + "{'voter_name':'any','guardian':'any'} where the voter_name and guardian key must come  and  pls not more extra text."
        response = GenerateGPTResponse(prompt)
        voter_name ,guardian = getVotterandGardian(response)
        context = {
            "voter_name": voter_name,
            "guardian": guardian,
            "block_code": block_code,
            "voter_number": voter_number,
            "pp": pp,
            "na": na,
            "booth_number": booth_number,
        }
      
        return render(request, self.template_name, context)
