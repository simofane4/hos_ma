
import random , string
from django.core.management.base import BaseCommand
from faker import Faker 
#from django.contrib.auth.models import User
from core.models import Assistant, Doctor, Patient, Specialite, Cabinet,User
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

list_specailite = [
'L allergologie ou l immunologie',
'L anesthésiologie',
'Landrologie',
'La cardiologie',
'La chirurgie',
'La chirurgie cardiaque',
'La chirurgie esthétique,plastique et reconstructive',
'La chirurgie générale',
'La chirurgie maxillo-faciale',
'La chirurgie pédiatrique',
'La chirurgie thoracique',
"La chirurgie vasculaire",
'La neurochirurgie',
'La dermatologie',
'L endocrinologie',
'La gastro-entérologie',
'La gériatrie',
'La gynécologie',
'L hématologie',
'L hépatologie',
'L infectiologie',
'La médecine aiguë',
'La médecine du travail',
'La médecine générale',
'La médecine interne',
'La médecine nucléaire',
'La médecine palliative',
'La médecine physique',
'La médecine préventive',
'La néonatologie',
'La néphrologie',
'La neurologie',
'L odontologie',
'L oncologie',
'L obstétrique',
'L ophtalmologie',
'L orthopédie',
'L Oto-rhino-laryngologie',
'La pédiatrie',
'La pneumologie',
'La psychiatrie',
'La radiologie',
'La radiothérapie',
'La rhumatologie',
'L urologie',
] 


gender_list = ['Male','Female']


class Command(BaseCommand):
    help = "Command information"
    def handle(self, *args, **kwargs):
        faker = Faker()
        for s in list_specailite:
            specialite = Specialite.objects.create(name = s)

        specialite = Specialite.objects.all().values_list('id' ,flat= True).distinct()
        print(specialite)
        
        
        for i in range(0,50):
            name = faker.name()
            first_name = name.split(' ')[0]
            last_name = ' '.join(name.split(' ')[-1:])
            try:                 
                username = first_name[0].lower() + last_name.lower().replace(' ', '')
                user = User.objects.create_user(username, password=username)               
            except IntegrityError as e :
                print( f"IntegrityError{e}" )
                username = first_name[0].lower() + last_name.lower().replace(' ', '') + random.choice(string.ascii_lowercase)
                user = User.objects.create_user(username, password=username)

            user.first_name = first_name
            user.last_name = last_name
            user.role = "doctor"
            user.is_superuser = False
            user.is_staff = False
            user.email = username + "@" + last_name.lower() + ".com"
            user.save()

            create_cabinet = Cabinet.objects.create(name='Doc  '+name, 
                                                    number=faker.phone_number(),
                                                    address=faker.address())
            last_cabinet = Cabinet.objects.last()
            print('last cabinet:', last_cabinet  )
            last_user = User.objects.last()
            
            
            print('last user id =' , last_user)
            get_specialite_id = random.choice(specialite)
            get_specialite = Specialite.objects.get(pk=get_specialite_id)
            create_doctor =  Doctor.objects.create(

                user=last_user,
                cabinet = last_cabinet,
                inp= faker.bothify(text='########'),
                gender= random.choice(gender_list),
                phone = faker.phone_number(),
                address = faker.address(),
                specialiste= get_specialite,

            )

            name_assistant = faker.name()
            first_name_assistant = name_assistant.split(' ')[0]
            last_name_assistant = ' '.join(name_assistant.split(' ')[-1:])

            try:                
                username_assistant = first_name_assistant[0].lower() + last_name_assistant.lower().replace(' ', '')
                user_assistant = User.objects.create_user(username_assistant, password=username_assistant)                
            except IntegrityError as e :
                print( f"IntegrityError{e}" )
                username_assistant = first_name_assistant[0].lower() + last_name_assistant.lower().replace(' ', '') + random.choice(string.ascii_lowercase)
                user_assistant = User.objects.create_user(username_assistant, password=username_assistant)
                
            user_assistant.first_name = first_name_assistant
            user_assistant.last_name = last_name_assistant
            user_assistant.is_superuser = False
            user_assistant.is_staff = False
            user_assistant.email = username_assistant + "@" + last_name_assistant.lower() + ".com"
            user_assistant.role = "assistant"
            user_assistant.save()

        
            last_user_assistant = User.objects.last()
            create_assistant=  Assistant.objects.create(

                user=last_user_assistant,
                cabinet = last_cabinet,
                gender= random.choice(gender_list),
                cin = faker.bothify(text='??######'),
                phone = faker.phone_number(),
                address = faker.address(),
            )

            for i in range(0,50):
                

                patient_name = faker.name()
                first_name_patient = patient_name.split(' ')[0]
                last_name_patient = ' '.join(patient_name.split(' ')[-1:])

                try:

                    username_patient = first_name_patient[0].lower() + last_name_patient.lower().replace(' ', '')
                    user_patient = User.objects.create_user(username_patient, password=username_patient)
                except IntegrityError as e :
                    print( f"IntegrityError{e}" )
                    username_patient = first_name_patient[0].lower() + last_name_patient.lower().replace(' ', '')+ random.choice(string.ascii_lowercase)
                    user_patient = User.objects.create_user(username_patient, password=username_patient)
                
                user_patient.first_name = first_name_patient
                user_patient.last_name = last_name_patient
                user_patient.is_superuser = False
                user_patient.is_staff = False
                user_patient.email = username_patient + "@" + last_name_patient.lower() + ".com"
                user_patient.role = "patient"
                user_patient.save()
                last_user_patient = User.objects.last()
                create_patient= Patient.objects.create(
                    user = last_user_patient,
                    cabinet=last_cabinet,
                    cin = faker.bothify(text='??######'),
                    address = faker.address(),
                    gender = random.choice(gender_list),
                    birthday = faker.date_of_birth(),
                    phone = faker.phone_number(),
                    
                )
                last_patient = Patient.objects.last()
                print(last_patient.id)

        