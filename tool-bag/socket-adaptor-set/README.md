# socket-adaptor-set

Parametric model for [Draper socket adaptor set](https://www.drapertools.com/product/00005/socket-adaptor-set-1-4-hex-x-1-4-3-8-1-2-sq-dr-3-piece/)

![Draper socket adaptor set image](https://cdn11.bigcommerce.com/s-1qmaqa25jp/images/stencil/640w/products/14910/50870/00005_BCS-3__59473.1642775545.jpg?c=1)

This directory holds the output of the python [cadquery](https://github.com/CadQuery/cadquery) script I used for [3D Printing](https://www.printables.com/model/268902-draper-socket-adaptor-set-holder).

## Configure

You simply want to change the parameters via the [config.yml file](https://github.com/MadeforMaking/organised/tree/master/tool-bag/socket-adaptor-set/cadquery/config.yml).

- Ensure the [requirements](https://github.com/MadeforMaking/organised/tree/master/tool-bag/socket-adaptor-set/cadquery/requirements.txt) (`requirements.txt`) are installed.
- Change directory to `socket-adapter-set.py` location.
- Make nessesary changes to neighbouring `config.yml`.
- Run `python socket-adapter-set.py`
- Enter file name (excluding extention) into the terminal input prompt.

You will obtain an `.stl` file to your configuration.

## View & Edit CodeCAD

If you want to tweak the CodeCAD logic.

I reccomend creating a separate [conda](https://docs.conda.io/en/latest/) enviroment for running [cq-editor](https://github.com/CadQuery/CQ-editor).

- [Install instructions](https://github.com/CadQuery/CQ-editor#installation-anaconda)
- Ensure the [requirements](https://github.com/MadeforMaking/organised/tree/master/tool-bag/socket-adaptor-set/cadquery/requirements.txt) (`requirements.txt`) are installed.

OR

- Use the [packate-list.txt](https://github.com/MadeforMaking/organised/tree/master/tool-bag/socket-adaptor-set/cadquery/package-list.txt) when [creating a new conda enviroment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
