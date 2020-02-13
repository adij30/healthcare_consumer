from django.shortcuts import render
from consumer_generic.generic_methods import *
from consumer_generic.all_classes import Hospital


def dummy_hospital():
    return Hospital(name='', phone_no='', address_id=0, id=0)


# def welcome_hospital(req):
#     return render(req, 'hospital.html', {'hospital_list': get_all_entities(entity='hospital'),
#                                         'hsp': dummy_hospital()})

def welcome_hospital(req):
    # print('*' * 30)
    # avl_address_list = get_all_entities(entity='address')
    # print("avl_address_list :")
    # for a in avl_address_list:
    #     print(a)
    # print('*' * 20)
    # avl_hospital_list = get_all_entities(entity='hospital')
    # print("avl_hospital_list :")
    # for h in avl_hospital_list:
    #     print(h)

    return render(req, 'hospital.html', {'hospital_list': get_all_entities(entity='hospital'),
                                         'hsp': dummy_hospital(),
                                         'address_list': get_all_entities(entity='address')})


def save_update(req):
    print('call to save_update')
    user_filled_data = req.POST
    hospital_id = int(user_filled_data['h_id'])
    hospital_obj = Hospital(name=user_filled_data['h_name'], phone_no=user_filled_data['h_phone_no'],
                            address_id=user_filled_data['address_id'])
    if hospital_id > 0:
        hospital_obj.id = hospital_id
        msg = update_entity(entity_object=hospital_obj)
        if msg.__contains__('id'):
            msg = f'Hospital with id {msg["id"]} updated successfully...'
    else:
        msg = save_entity(entity_object=hospital_obj)
        print("***save msg***", msg)
        if msg.__contains__('id'):
            msg = 'Hospital added successfully...'

    return render(req, 'hospital.html', {'hospital_list': get_all_entities(entity='hospital'),
                                         'hsp': dummy_hospital(),'action': msg,
                                         'address_list': get_all_entities(entity='address')})


def edit(req, id):

    return render(req, 'hospital.html', {'hospital_list': get_all_entities(entity='hospital'),
                                         'hsp': get_single_entity(entity='hospital', entity_id=id),
                                         'address_list': get_all_entities(entity='address')})


def delete(req, id):
    msg = delete_entity(entity_type='hospital', entity_id=id)
    return render(req, 'hospital.html',
                  {'hospital_list': get_all_entities(entity='hospital'),
                   'address_list': get_all_entities(entity='address'),
                   'adr': dummy_hospital(), 'action': msg})

# def available_address_list(req):
#     print('*'*15)
#     avl_address_list = get_all_entities(entity='address')
#     print("avl_address_list :", avl_address_list)
#     print('*' * 15)
#     return render(req, 'hospital.html', {'hospital_list': get_all_entities(entity='hospital'),
#                                          'hsp': dummy_hospital(),
#                                          })