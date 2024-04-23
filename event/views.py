from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages  # Import the messages module
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # Import the mixins
from .models import Event
from django.forms import DateInput


class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Event
    template_name = 'event/event_form.html'
    fields = ['title', 'description', 'date', 'participants', 'location']
    success_url = reverse_lazy('event_list') 
    permission_required = 'event.add_event'  # Adjust with the appropriate permission codename

    def form_valid(self, form):
        messages.success(self.request, 'Event created successfully')  # Add success message
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file'] = 'css/event_form.css'  # Provide the CSS file path to the template
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name in form.fields:
            form.fields[field_name].widget.attrs['class'] = 'form-control'
        form.fields['date'].widget = DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for event in context['events']:
            event.time_since_creation = self.get_time_since_creation(event.created_at)
        return context

    def get_time_since_creation(self, created_at):
        time_since = timezone.now() - created_at
        seconds = abs(time_since.total_seconds())
        if seconds < 60:
            return f"{int(seconds)} seconds"
        minutes = seconds / 60
        if minutes < 60:
            return f"{int(minutes)} minutes"
        hours = minutes / 60
        if hours < 24:
            return f"{int(hours)} hours"
        days = hours / 24
        if days < 365:
            return f"{int(days)} days"
        return "Over a year ago"

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'

class EventUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Event
    template_name = 'event/event_form.html'
    fields = ['title', 'description', 'date', 'participants', 'location']
    permission_required = 'event.change_event'  # Adjust with the appropriate permission codename

    def get_success_url(self):
        messages.success(self.request, 'Event updated successfully')  # Add success message
        return reverse_lazy('event_list')


class EventDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy('event_list')
    permission_required = 'event.delete_event'  # Adjust with the appropriate permission codename

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Event deleted successfully')  # Add success message
        return super().delete(request, *args, **kwargs)
