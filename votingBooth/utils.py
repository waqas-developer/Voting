# views.py
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
# import cStringIO as StringIO
from io import StringIO
from io import BytesIO 
from django.template import Context
from html import escape

def generate_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html = template.render(context)

    result = BytesIO()  # Use BytesIO instead of StringIO
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)  # Encode the HTML content to bytes and pass it to BytesIO

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return HttpResponse("We had some errors<pre>%s</pre>" % html)