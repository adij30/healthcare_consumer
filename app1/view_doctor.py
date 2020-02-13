from django.shortcuts import render
from consumer_generic.generic_methods import *
from consumer_generic.all_classes import Doctor


def dummy_doctor():
    return Doctor(name='', speciality='', experience=0, salary=0, email='', blog='', hospital_id='', id=0)


def welcome_doctor(req):
    return render(req, 'doctor.html', {'hospital_list': get_all_entities(entity='hospital'),
                                       'doctor_list': get_all_entities(entity='doctor'),
                                       'doc': dummy_doctor()})


def edit(req, id):

    return render(req, 'doctor.html', {'hospital_list': get_all_entities(entity='hospital'),
                                       'doctor_list': get_all_entities(entity='doctor'),
                                       'doc': get_single_entity(entity='doctor', entity_id=id),
                                       })


def delete(req, id):
    msg = delete_entity(entity_type='doctor', entity_id=id)
    return render(req, 'doctor.html', {'hospital_list': get_all_entities(entity='hospital'),
                                       'doctor_list': get_all_entities(entity='doctor'),
                                       'doc': dummy_doctor(), 'action': msg
                                       })


def save_update(req):
    print('call to save_update')
    user_filled_data = req.POST
    doctor_id = int(user_filled_data['d_id'])
    doctor_obj = Doctor(name=user_filled_data['d_name'], speciality=user_filled_data['d_speciality'],
                        experience=user_filled_data['d_experience'], salary=user_filled_data['d_salary'],
                        email=user_filled_data['d_email'], blog=user_filled_data['d_blog'],
                        hospital_id=user_filled_data['hospital_id'])
    if doctor_id > 0:
        doctor_obj.id = doctor_id
        msg = update_entity(entity_object=doctor_obj)
        if msg.__contains__('id'):
            msg = f'Doctor with id {msg["id"]} updated successfully...'
    else:
        msg = save_entity(entity_object=doctor_obj)
        print("***save msg***", msg)
        if msg.__contains__('id'):
            msg = 'Doctor added successfully...'

    return render(req, 'doctor.html', {'hospital_list': get_all_entities(entity='hospital'),
                                       'doctor_list': get_all_entities(entity='doctor'),
                                       'action': msg,
                                       'doc': dummy_doctor()})
