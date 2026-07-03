
import os
import importlib



def load_plugins():

    result=[]


    for file in os.listdir("plugins"):


        if file.endswith(".py") and file!="__init__.py":


            result.append(
            file[:-3]
            )


    return result




def run_plugin(name, target=None):


    module=importlib.import_module(
    "plugins."+name
    )


    if target:

        return module.run(target)


    return module.run()

