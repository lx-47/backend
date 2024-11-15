from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CourseEnrollment, Lesson, Section, Student, StudentAssessment

@receiver(post_save, sender=CourseEnrollment)
def add_course_to_student_enrolled_courses(sender, instance, created, **kwargs):
    if created and instance.validity: 
        instance.student.courses_enrolled.add(instance.course)

@receiver(post_delete, sender=CourseEnrollment)
def remove_course_from_student_enrolled_courses(sender, instance, **kwargs):
    instance.student.courses_enrolled.remove(instance.course)

@receiver(post_save, sender=Lesson)
@receiver(post_delete, sender=Lesson)
def update_section_duration(sender, instance, **kwargs):
    section = instance.section
    section.duration = section.total_duration()
    section.save()

@receiver(post_save, sender=Section)
@receiver(post_delete, sender=Section)
def update_course_duration(sender, instance, **kwargs):
    # Get the course related to this section
    course = instance.course
    # Recalculate the total duration for the course
    course.duration = course.total_duration()
    # Save the updated course instance
    course.save()

@receiver(post_save, sender=StudentAssessment)
def update_reward_points_on_save(sender, instance, **kwargs):
    if instance.is_completed:
        score = instance.score
        rewardPoints = score // 2
        user = instance.user
        student = Student.objects.get(user = user)
        student.rewardPoints += rewardPoints
        student.save()

