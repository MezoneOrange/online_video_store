from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    """Data base for courses.

    Fields:

        slug - slug field, contains full url address for course in the site (special technology for create slug links).
               /course/slug_name

        title - char field, course's name. Max length is 120 symbols.

        description - text field, course's description.

        image - image field, course's image. If course won't have an special image, it would be assigned default image.
                default - /media/default.png
                special image - /media/course_images/image

        free - boolean field, type of course. If course is free - True, otherwise - False.

    """
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(default='default.png', upload_to='course_images/', blank=True)
    free = models.BooleanField(default=True)

    def __str__(self):
        """It will print course's name."""
        return self.title

    def get_absolute_url(self):
        """Returns absolute item's url address for create url for every item.

        Function reverse:
            reverse(name, dict)

            1. name - name which we create for the page in urls.py

            2. dict - kwargs={ key - name position where we refer
                               value - which value we'll send to key position.}

        In other words it will add 'slug' value of item to url, that was written in file urls.py with given 'name'.
        """
        return reverse('course-detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    """Data base for course lessons.

    Fields:

        slug - slug field, contains full url address for lesson in the site (special technology for create slug links).
               /course/course/slug_name

        title - char field, course's name. Max length is 120 symbols.

        description - text field, course's description.

        course - connects lesson with course from Course database. When course would be delete -
        lessons that were connected with it will deleted. (on_delete=models.SET_NULL, null=True)

        number - integer field, number of lesson.

        video_url - char field, url for lesson's video. Max length is 100 symbols.
    """
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):
        """It will print course's name."""
        return self.title

    def get_absolute_url(self):
        """Returns absolute item's url address for create url for every item.

        Function reverse:
            reverse(name, dict)

            1. name - name which we create for the page in urls.py

            2. dict - kwargs={ key - name position where we refer
                               value - which value we'll send to key position.}

        In other words it will add key's value of item to url, that was written in file urls.py with given 'name'.
        """
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})
