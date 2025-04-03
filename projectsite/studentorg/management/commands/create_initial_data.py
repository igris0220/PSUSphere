from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.fake = Faker()
        self.fake_ph = Faker('en_PH')
        self.create_organizations(10)
        self.create_students(50)
        self.create_membership(10)

    def create_organizations(self, count):
        colleges = list(College.objects.all())
        if not colleges:
            self.stdout.write(self.style.WARNING('No colleges found. Organizations cannot be created.'))
            return

        organizations = [
            Organization(
                name=' '.join(self.fake.words(2)).title(),
                college=self.fake.random_element(colleges),
                description=self.fake.sentence()
            )
            for _ in range(count)
        ]
        Organization.objects.bulk_create(organizations)
        self.stdout.write(self.style.SUCCESS('Initial data for organizations created successfully.'))

    def create_students(self, count):
        programs = list(Program.objects.all())
        if not programs:
            self.stdout.write(self.style.WARNING('No programs found. Students cannot be created.'))
            return

        students = [
            Student(
                student_id=f'{self.fake_ph.random_int(2020, 2024)}-{self.fake_ph.random_int(1, 8)}-{self.fake_ph.random_number(digits=4)}',
                lastname=self.fake_ph.last_name(),
                firstname=self.fake_ph.first_name(),
                middlename=self.fake_ph.last_name(),
                program=self.fake.random_element(programs)
            )
            for _ in range(count)
        ]
        Student.objects.bulk_create(students)
        self.stdout.write(self.style.SUCCESS('Initial data for students created successfully.'))

    def create_membership(self, count):
        students = list(Student.objects.all())
        organizations = list(Organization.objects.all())

        if not students or not organizations:
            self.stdout.write(self.style.WARNING('No students or organizations found. Memberships cannot be created.'))
            return

        memberships = [
            OrgMember(
                student=self.fake.random_element(students),
                organization=self.fake.random_element(organizations),
                date_joined=self.fake.date_between(start_date='-2y', end_date='today')
            )
            for _ in range(count)
        ]
        OrgMember.objects.bulk_create(memberships)
        self.stdout.write(self.style.SUCCESS('Initial data for student memberships created successfully.'))