from django.shortcuts import render
from django.views import View

from wikipedia_links.settings import BASE_DIR
from . import logic
import os

from django.http import HttpResponse, Http404


def download_log_file(request):
    log_file_path = os.path.join(BASE_DIR, 'wiki_search.log')
    if os.path.exists(log_file_path):
        with open(log_file_path, 'rb') as log_file:
            response = HttpResponse(log_file.read())
            response['Content-Type'] = 'text/plain'
            response['Content-Disposition'] = 'attachment; filename=debug.log'
            return response
    else:
        return HttpResponse('Лог-файл не найден', status=404)

        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=myapp.log'

        return response


class WikipediaLinks(View):
    template_name = "wikipedia/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        link1, link2 = request.POST.get('link1'), request.POST.get('link2')
        my_data = logic.main(str(link1), str(link2))
        return render(request, self.template_name, {'my_data': my_data, "log_file": True})