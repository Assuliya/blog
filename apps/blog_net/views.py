from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import Entry
from forms import ContactForm
from django.core.mail import send_mail, mail_admins
import signals
from django.db.models import Max, Min, Avg, Count
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    entries = Entry.objects.published_entries().order_by('-id')
    paginator = Paginator(entries, 2)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page = paginator.page(1)
    ctx = { 'page': page}
    return render(request, 'blog_net/index.html', ctx)

def about(request):
    # ctx = { 'entries': entries}
    return render(request, 'blog_net/about.html')

def archive(request):
    base_qs = Entry.objects.filter(published=True)
    in_archive = base_qs.aggregate(count=Count('pk'), max=Max('pk'), min=Min('pk'), avg=Avg('pk'))
    month = connection.ops.date_trunc_sql('month', 'created')
    per_month_count = base_qs.extra({'date':month}).values('date').annotate(count=Count('pk')).order_by('date')
    ctx = { 'in_archive': in_archive,
            'per_month_count': per_month_count,
            'base_qs':base_qs
    }
    return render(request, 'blog_net/archive.html', ctx)

def contact(request):
    success = False
    email = ''
    title = ''
    text = ''
    contact_sent = request.session.get('contact_sent', False)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            print "WORKED"
        else:
            print "DID NOT WORK"
        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']

            request.session['contact_sent'] = True
            # send_mail("Message from Blog","title: %s \ntext: %s \nemail: %s" %(title,text,email), "sends from my email to mine", [settings.EMAIL_HOST_USER])

            signals.message_sent.send(sender=ContactForm, email=email)
    else:
        contact_form = ContactForm()
    ctx = { 'contact_form': contact_form, 'contact_sent':contact_sent, 'email': email, 'title': title, 'text': text, 'success': success}
    request.session.set_test_cookie()
    return render(request, 'blog_net/contact.html', ctx)
