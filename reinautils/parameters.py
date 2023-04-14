# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_Parameters.ipynb.

# %% auto 0
__all__ = ['Parameters']

# %% ../nbs/00_Parameters.ipynb 3
import json

# %% ../nbs/00_Parameters.ipynb 4
class Parameters():
    '''A splecial class whos atributes can be referenced as attributs or as dictionaty keys'''

    def __init__(self, **kargs):
        self.add_attr(**kargs)

    def __call__(self, param, value=None):
        if value is not None:
            setattr(self, param, value)
        return self.__getattribute__(param)

    def __repr__(self):
        str_out = f'{self.__class__}'
        for key, value in self.__dict__.items():
            str_out += f'\n   {key} : '+'\n   '.join([i for i in repr(value).split('\n')]) if isinstance(value,Parameters) else f'\n   {key} : {repr(value)}'
        return str_out

    def __str__(self):
        str_out = 'Parameters:'
        for key,value in self.__dict__.items():
            str_out += f'\n   {key} : '+'\n   '.join([i for i in str(value).split('\n')]) if isinstance(value,Parameters) else f'\n   {key} : {value}'
        return str_out

    def add_attr(self, **kargs):
        '''Add attributes to the Parameters class, this will be done recursivly'''
        for key, value in kargs.items():
            if isinstance(value, dict):
                setattr(self, key, Parameters(**value))
            else:
                setattr(self, key, value)

    def to_dict(self):
        '''Convert the parameters to dictionary recorsively'''
        return {key:value if not isinstance(value,Parameters) else value.to_dict() for key,value in self.__dict__.items()}

    def __len__(self) -> int:
        return len(self.__dict__ )

    def __getitem__(self, key):
        return self.__getattribute__(key)

    def __setitem__(self, key, value):
        self.add_attr(**{key: value})

    def __delitem__(self, key):
        delattr(self, key)

    def from_json(self, json_file_name:str):
        '''Read json file and add to parameters'''
        with open(json_file_name) as json_data_file:
            data = json.load(json_data_file)
        self.add_attr(**data)
        return self
