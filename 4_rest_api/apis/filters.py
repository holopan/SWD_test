import django_filters
from .models import School, Classroom, Teacher, Student

class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(django_filters.FilterSet):
    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classrooms__school', distinct=True)
    classroom = django_filters.NumberFilter(field_name='classrooms', distinct=True)
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']

class StudentFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classroom__school')
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']