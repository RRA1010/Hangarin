from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from hangarin.models import Priority, Category,Task, Note, SubTask

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_task(20)
        self.create_notes(10)
        self.create_subtask(5)
    
    def create_task(self, count):
        fake = Faker()

        for _ in range(count):
            sentence = [fake.sentence(nb_words=5) for _ in range(5)]
            task_name = ' '.join(sentence)
            Task.objects.create(
                title=task_name.title(),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending","In Progress,","Completed"]),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first(),
                )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for task created successfully.'
        ))
        
    def create_notes(self, count):
        fake = Faker()
        for _ in range(count):
            Note.objects.create(
                task=Task.objects.order_by('?').first(),
                content=fake.paragraph(nb_sentences=3),
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for notes created successfully.'
        ))

    def create_subtask(self,count):
        fake = Faker()

        for _ in range(count):
            SubTask.objects.create(
                parent_task=Task.objects.order_by('?').first(),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=["Pending","In Progress,","Completed"])
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for sub-task created successfully.'
        ))



                
