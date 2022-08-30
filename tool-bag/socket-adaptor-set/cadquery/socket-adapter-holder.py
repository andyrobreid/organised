"""
Name: 'Andrew "MadeforMaking" Reid'

Github: https://github.com/MadeforMaking

Links: 
    - https://github.com/MadeforMaking/organised/tree/master/tool-bag/socket-adaptor-set
    - https://www.drapertools.com/product/00005/socket-adaptor-set-1-4-hex-x-1-4-3-8-1-2-sq-dr-3-piece/
"""
from math import pi
from cadquery import cq, exporters
from yaml import load, Loader

with open("./config.yml", "r") as stream:
    CFG = load(stream, Loader)

box = (
    cq.Workplane("XY")
    .box(CFG["THICKNESS"], CFG["WIDTH"], CFG["HEIGHT"], centered=(True, False, True))
    .translate((0, -10, 0))
    .edges("|X").fillet(CFG["RADIUS"])
)

def head(size: str):
    cfg = CFG["DIM"][size]
    thickness = CFG["THICKNESS"]
    x = cfg["head"]["width"] + CFG["TOLERANCE"]
    obj = (
        cq.Workplane("XY")
        .box(thickness, x, x)
        .faces(">Y").workplane(offset=-cfg["head"]["divet"]/pi)
        .sphere(cfg["head"]["divet"])
        .edges("|X").fillet(CFG["RADIUS"]/8)
    )
    return obj

y = 0
heads = []
for i in CFG["DIM"].keys():
    result = head(i).translate((0, y, 0))
    heads.append(result)
    y = y + CFG["DIM"][i]["head"]["width"]*1.5

result = box

for shape in heads: 
    result = result.cut(shape)

if "show_object" in locals():
    show_object(result)
else:
    filename = input("Enter filename (excluding extention):")
    exporters.export(result, f'{filename}.stl', exportType="STL")