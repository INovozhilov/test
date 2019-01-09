from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db import transaction
from datetime import datetime

from .models import Subscription, Visit
from .form import VisitReportForm

class Index(generic.ListView):
    # template_name = 'polls/index.html'
    # context_object_name = 'latest_question_list'
    model = Subscription

    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]


class Detail(generic.DetailView):
    model = Subscription


@transaction.atomic
def mark(request, qrcode):
    subscription = get_object_or_404(Subscription, qrcode=qrcode)

    subscription.visit_set.create(date=datetime.now())
    subscription.count_left -= 1
    subscription.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('scan:scan', args=(qrcode,)))


class SubscriptionCreate(CreateView):
    model = Subscription
    fields = '__all__'


class SubscriptionUpdate(UpdateView):
    model = Subscription
    fields = '__all__'


class SubscriptionDelete(DeleteView):
    model = Subscription
    success_url = reverse_lazy('index')


def scan(request, pk=None):
    if pk is not None:
        subscription = Subscription.objects.get(pk=pk)
        # visits = Visit.objects.all()
        context = {'subscription': subscription, }
    else:
        subscriptions = Subscription.objects.all()
        context = {'subscription_list': subscriptions, }

    return render(request, 'scan/scan.html', context=context)


def visitreport(request):
    form = VisitReportForm(request.GET)
    context = {'form': form}
    date = request.GET.get('date', None)
    if date is not None:
        context['subscription_list'] = Subscription.objects.filter(visit__date=date)
    context['date_param'] = date

    return render(request, 'scan/visitreport.html' , context=context)
