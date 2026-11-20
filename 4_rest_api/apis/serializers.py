from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

# --- Simple Serializers  ---
class ClassroomSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'grade', 'room']

class TeacherSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender']

class StudentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'firstname', 'lastname', 'gender']

# --- School Serializers ---
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']

class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()


# --- Classroom Serializers ---
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'grade', 'room']

class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSimpleSerializer(many=True, read_only=True)
    students = StudentSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'school', 'grade', 'room', 'teachers', 'students']


# --- Teacher Serializers ---
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender', 'classrooms']

class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender', 'classrooms']


# --- Student Serializers ---
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'classroom', 'firstname', 'lastname', 'gender']

class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = ClassroomSimpleSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'classroom', 'firstname', 'lastname', 'gender']