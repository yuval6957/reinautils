# reinautils

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## The Utilities included are:

------------------------------------------------------------------------

<a
href="https://github.com/yuval6957/reinautils/blob/main/reinautils/parameters.py#LNone"
target="_blank" style="float:right; font-size:smaller">source</a>

### Parameters

>      Parameters (**kargs)

A splecial class whos atributes can be referenced as attributs or as
dictionaty keys

## Install

``` sh
pip install reinautils
```

## How to use

### Parameters

You can create a Parameters class from dict

``` python
params=Parameters(first=1,second='A')
print(params.first)
```

    1

You can also creat a Parameters class and populate it from a json file

``` python
params2=Parameters().from_json('config_demo.json')
print(params2)
```

    Parameters:
       path : Parameters:
          data : /workspace/hd/
          tmp : /workspace/hd/tmp/
          features : /workspace/nvme/features/
          train : /workspace/nvme/train/
          models : /workspace/hd/models/
          output : /workspace/hd/outputs/
          test : /workspace/nvme/test/
       platform : myserver
