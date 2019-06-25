from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import ServerInfo
from .forms import ServerForm
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class ServerInfoView(View):
    template_name = "server.html"

    def get_context(self):
        server = ServerInfo.get_all()
        try:
            page = self.request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(server, 10, request=self.request)
        page_list = p.page(page)

        context = {
            #'server_context': server,
            'p': p,
            'page_list': page_list
        }
        return context

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context=context)


class ServerCreateView(View):
    template_name = "server_create.html"

    def get(self, request):
        form = ServerForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('server'))

        return render(request, self.template_name, context={'form': form})
