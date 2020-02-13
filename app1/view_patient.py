from django.shortcuts import render
from consumer_generic.generic_methods import *
from consumer_generic.all_classes import Patient


def convert_date_format(date):
    if not '-' in date:
        l1 = date.split('/')
        l1 = l1[::-1]
        l1[1],l1[2] = l1[2],l1[1]#swap month and date
        date = '-'.join(l1)
        # print('date', date)
        return date
    return date


def dummy_patient():
    return Patient(name='', gender='', birth_date='', blood_group='', diseases='', address_id='', doctor_id='', id=0)


def welcome_patient(req):
    return render(req, 'patient.html', {'patient_list': get_all_entities(entity='patient'),
                                        'address_list': get_all_entities(entity='address'),
                                        'doctor_list': get_all_entities(entity='doctor'),
                                        'pat': dummy_patient()})


def edit(req, id):

    return render(req, 'patient.html', {'patient_list': get_all_entities(entity='patient'),
                                        'address_list': get_all_entities(entity='address'),
                                        'doctor_list': get_all_entities(entity='doctor'),
                                        'pat': get_single_entity(entity='patient', entity_id=id),
                                       })


def delete(req, id):
    msg = delete_entity(entity_type='patient', entity_id=id)
    return render(req, 'patient.html', {'patient_list': get_all_entities(entity='patient'),
                                        'address_list': get_all_entities(entity='address'),
                                        'doctor_list': get_all_entities(entity='doctor'),
                                        'pat': dummy_patient()})


def save_update(req):
    print('call to save_update')
    user_filled_data = req.POST
    doc_ids = req.POST.getlist('doc_ids')
    for i in doc_ids:
        if i is '':
            doc_ids.remove('')
    print('user_filled_data: ',user_filled_data)
    patient_id = int(user_filled_data['p_id'])
    patient_obj = Patient(name=user_filled_data['p_name'], gender=user_filled_data['p_gender'],
                          birth_date=convert_date_format(user_filled_data['p_dob']), blood_group=user_filled_data['p_bloog_group'],
                          diseases=user_filled_data['p_diseases'], address_id=user_filled_data['adr_id'],
                          doctor_id=doc_ids)

    if patient_id > 0:
        patient_obj.id = patient_id
        msg = update_entity(entity_object=patient_obj)
        if msg.__contains__('id'):
            msg = f'Patient with id {msg["id"]} updated successfully...'
    else:
        msg = save_entity(entity_object=patient_obj)
        print("***save msg***", msg)
        if msg.__contains__('id'):
            msg = 'Patient added successfully...'

    return render(req, 'patient.html', {'patient_list': get_all_entities(entity='patient'),
                                        'address_list': get_all_entities(entity='address'),
                                        'doctor_list': get_all_entities(entity='doctor'),
                                        'pat': dummy_patient(),'action': msg})
