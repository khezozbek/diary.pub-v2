from .models import Teacher, Parent, ExamResult, CustomUser, Student, ScoreHistory
from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_students(sender, instance, created, **kwargs):
    if created and instance.type == 'Student':
        student = Student.objects.create(user=instance)
        student.save()


@receiver(pre_save, sender=ScoreHistory)
def update_score_history(sender, instance, **kwargs):
    instance.month = instance.student.level
    instance.save()


@receiver(pre_save, sender=Student)
def create_score_history(sender, instance, **kwargs):
    if instance.id is None:
        current_month = datetime.now().strftime("%B")
        exam_result = ExamResult.objects.filter(student=instance, month=current_month, score=instance).first()
        score = exam_result.score if exam_result else 0
        score_history = ScoreHistory(student=instance, month=current_month, score=score)
        score_history.save()


@receiver(post_save, sender=CustomUser)
def create_teacher(sender, instance, created, **kwargs):
    if created and instance.type == 'Teacher':
        Teacher.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def create_parent(sender, instance, created, **kwargs):
    if created and instance.type == "Parent":
        Parent.objects.create(user=instance)
