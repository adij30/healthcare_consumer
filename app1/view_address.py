from django.shortcuts import render
from consumer_generic.generic_methods import *
from consumer_generic.all_classes import Address

# Create your views here.


def dummy_address():
    return Address(city='', state='', pincode=0, id=0)


def welcome_clc(req):
    return render(req, 'welcome.html')


def welcome_address(req):

    return render(req, 'address.html', {'address_list': get_all_entities(entity='address'),
                                        'adr': dummy_address()})


def save_update(req):
    print('call to save_update')
    user_filled_data = req.POST
    address_id = int(user_filled_data['a_id'])
    address_obj = Address(city=user_filled_data['a_city'], state=user_filled_data['a_state'],
                                                        pincode=user_filled_data['a_pincode'])
    if address_id > 0:
        address_obj.id = address_id
        msg = update_entity(entity_object=address_obj)
        print('*'*20,msg,type(msg))
        if msg.__contains__('id'):
            msg = f'Address with id {msg["id"]} updated successfully...'
    else:
        msg = save_entity(entity_object=address_obj)
        if msg.__contains__('id'):
            msg = 'Address added successfully...'

    return render(req, 'address.html',
                  {'address_list': get_all_entities(entity='address'),
                   'adr': dummy_address(),
                   'action': msg})


def edit(req, id):
    return render(req, 'address.html',
                  {'address_list': get_all_entities(entity='address'),
                   'adr': get_single_entity(entity='address', entity_id=id)})


def delete(req, id):
    msg = delete_entity(entity_type='address', entity_id=id)
    return render(req, 'address.html',
                   {'address_list': get_all_entities(entity='address'),
                    'adr': dummy_address(), 'action': msg})