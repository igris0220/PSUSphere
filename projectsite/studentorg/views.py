
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, Program, College #,Boat
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, ProgramForm, CollegeForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

# Create your views here.

@method_decorator(login_required, name='dispatch')

class HomePageView(ListView):
    model = Student 
    context_object_name = 'home'
    template_name = "home.html"

class Organizationlist(ListView):
    model = Organization
    content_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(Organizationlist, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query)|
                           Q(college__college_name__icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

    def form_valid(self, form):
        organization_name = form.instance.name
        messages.success(self.request, f"{organization_name} has been added successfully.")
        return super().form_valid(form)

class OrganizationUpdateView(UpdateView):
    model = Organization
    fields = "__all__"
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

    def form_valid(self, form):
        organization_name = form.instance.name
        messages.success(self.request, f"{organization_name} has been Updated.")
        return super().form_valid(form)

class OrganizationDeleteView(DeleteView):
    model = Organization
#    form_class = OrganizationForm
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

    def form_valid(self, form):
        messages.success(self.request, f"Organization has been Deleted.")
        return super().form_valid(form)

class OrgMemberlist(ListView):
    model = OrgMember
    content_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5
    ordering = ['date_joined']

    def get_queryset(self, *args, **kwargs):
        qs = super(OrgMemberlist, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(date_joined__icontains=query)|Q(student__firstname__icontains=query)|
                           Q(student__lastname__icontains=query)|Q(organization__name__icontains=query))
        return qs

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        org_member = form.instance
        messages.success(self.request, f"{org_member} has been added successfully.")
        return super().form_valid(form)

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = "__all__"
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        org_member = form.instance
        messages.success(self.request, f"{org_member} has been Updated.")
        return super().form_valid(form)

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
#    form_class = OrgMemberForm
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        messages.success(self.request, f"Member has been Deleted.")
        return super().form_valid(form)

class StudentList(ListView):
    model = Student
    content_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student_id__icontains=query) | Q(firstname__icontains=query) |
                            Q(lastname__icontains=query) | Q(middlename__icontains=query) |
                            Q(program__prog_name__icontains=query))
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        id_student = form.instance.student_id
        messages.success(self.request, f"Student: {id_student} has been added successfully.")
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        id_student = form.instance.student_id
        messages.success(self.request, f"Student: {id_student} has been Updated.")
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
#    form_class = StudentForm
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, f"Student Deleted successfully.")
        return super().form_valid(form)


class ProgramList(ListView):
    model = Program
    content_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(ProgramList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(prog_name__icontains=query)|Q(college__college_name__icontains=query))
        return qs

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        program_name = form.instance.prog_name
        messages.success(self.request, f"Program: {program_name} has been added successfully.")
        return super().form_valid(form)

class ProgramUpdateView(UpdateView):
    model = Program
    fields = "__all__"
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        program_name = form.instance.prog_name
        messages.success(self.request, f"Program: {program_name} has been Updated.")
        return super().form_valid(form)

class ProgramDeleteView(DeleteView):
    model = Program
#    form_class = ProgramForm
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        messages.success(self.request, f"Program Deleted successfully.")
        return super().form_valid(form)

class CollegeList(ListView):
    model = College
    content_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

    def form_valid(self, form):
        name_college = form.instance.college_name
        messages.success(self.request, f"{name_college} has been added successfully.")
        return super().form_valid(form)

class CollegeUpdateView(UpdateView):
    model = College
    fields = "__all__"
    context_object_name = "college"
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

    def form_valid(self, form):
        college_name = form.instance.college_name
        messages.success(self.request,f'{college_name} has been Updated.')

        return super().form_valid(form)

class CollegeDeleteView(DeleteView):
    model = College
    #form_class = CollegeForm
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

    def form_valid(self, form):
        messages.success(self.request, f"College Deleted successfully.")
        return super().form_valid(form)

#class BoatCreateView(CreateView):
#    model = Boat
#    fields = "__all__"
#    template_name = "boat_form.html"
#    success_url = reverse_lazy('boat-list')
#    
#    def post(self, request, *args, **kwargs):
#        length = request.POST.get('length')
#        width = request.POST.get('width')
#        height = request.POST.get('height')
#        
#        # Validate dimensions
#        errors = []
#        for field_name, value in [('length', length), ('width', width), ('height', height)]: 
#            try:
#                if float(value) <= 0:
#                    errors.append(f"{field_name.capitalize()} must be greater than 0.")
#            except (ValueError, TypeError):
#                errors.append(f"{field_name.capitalize()} must be a valid number.")
#            
#        # If errors exist, display them and return to the form
#        if errors:
#            for error in errors:
#                messages.error(request, error)
#            return self.form_invalid(self.get_form())
#        # Call the parent's post() if validation passes
#        return super().post(request, *args, **kwargs)
#
#class BoatUpdateView(UpdateView):
#    model = Boat
#    fields = "__all__"
#    template_name = "boat_form.html"
#    success_url = reverse_lazy('boat-list')
#    
#    def post(self, request, *args, **kwargs):
#        length = request.POST.get('length')
#        width = request.POST.get('width')
#        height = request.POST.get('height')
#        
#        # Validate dimensions
#        errors = []
#        for field_name, value in [('length', length), ('width', width), ('height', height)]: 
#            try:
#                if float(value) <= 0:
#                    errors.append(f"{field_name.capitalize()} must be greater than 0.")
#            except (ValueError, TypeError):
#                errors.append(f"{field_name.capitalize()} must be a valid number.")
# 
#        # If errors exist, display them and return to the form
#        if errors:
#            for error in errors:
#                messages.error(request, error)
#            return self.form_invalid(self.get_form())
#        
#        # Call the parent's post() if validation passes
#        return super().post(request, *args, **kwargs)
