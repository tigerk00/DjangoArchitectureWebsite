from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import ContactInfo, ContactEmail


def contact(request):

    if request.method == "POST":
        cont_email = ContactEmail()
        name, email, message = request.POST.get("name"), request.POST.get("email"), request.POST.get("message")
        cont_email.name, cont_email.email, cont_email.message = name, email, message
        cont_email.save()
        messages.info(request, "✔️ Ваше сообщение было успешно доставлено!")
        return HttpResponseRedirect(request.path_info)

    contact_info = ContactInfo.objects.last()
    context = {"contact_info": contact_info}
    if contact_info.iframe_map:
        context["map"] = mark_safe(contact_info.iframe_map.replace('width="600"','width="450"'))
    return render(request,"contactsite/index.html", context)

