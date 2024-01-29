from django.db import models

NATIONALITIES = [
    ('USA', 'United States'),
    ('CAN', 'Canada'),
    ('RUS', 'Russia'),
    ('UK', 'United Kingdom')
]

class FighterBelt(models.Model):
    BELT = [
        ('Master', 'Master'),
        ('Champ', 'Champ'),
        ('Grapler', 'Grapler')
    ]
    belt = models.CharField(max_length=10, choices=BELT)

    def __str__(self):
        return f'{self.belt}'


class FightingStyle(models.Model):
    FIGHTING_STYLE_CHOICES =[
        ('Kickboxing', 'Kickboxing'),
        ('Muay Thai', 'Muay Thai'),
        ('Boxing', 'Boxing'),
        ('Jiu-Jitsu', 'Jiu-Jitsu'),
        ('Wrestling', 'Wrestling'),
    ]
    fight_style = models.CharField(max_length=50, choices=FIGHTING_STYLE_CHOICES, unique=True)

    def __str__(self):
        return f'{self.fight_style}'


class Fighter(models.Model):
    name = models.CharField(max_length=32, unique=True)
    country = models.CharField(max_length=3, choices=NATIONALITIES)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    record = models.CharField(max_length=8)
    profile_picture = models.ImageField(upload_to='pictures', null=True, blank=True)
    belt = models.OneToOneField(FighterBelt, on_delete=models.CASCADE, null=True, blank=True)
    fighting_styles = models.ManyToManyField(FightingStyle, related_name='fighters', blank=True)

    def __str__(self):
        return f'{self.name}, {self.country}'

class Comment(models.Model):
    comment = models.TextField(default="", blank=True)
    mark = models.PositiveSmallIntegerField(default=5)
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE, null=True, blank=True)
