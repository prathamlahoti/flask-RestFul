from typing import Dict

# Data Actions
RESULT_STATUS: Dict[str, str] = {
    'UPDATED': 'Hero information has been updatedUpdated',
    'DELETED': 'Hero Deleted',
    'NOT_FOUND': 'Hero Not Found'
}


def data_template(data: Dict) -> Dict[str, str]:
    """ Returns API's working keys with appropriate data

        :param data:
     """
    try:
        data = {
            'actor_name': data['actor_name'],
            'hero_name': data['hero_name'],
            'hero_rate': data['hero_rate']
        }
    except KeyError as ex:
        print(ex)
    else:
        return data
