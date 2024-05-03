import os
import json
from extensions import db
from functools import reduce
from flask_sqlalchemy import SQLAlchemy
from models import Product, ProductColor, ProductSize, ProductImage


def get_base_dir() -> str:
    return os.path.abspath('.')


def load_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    

# https://stackoverflow.com/questions/25833613/safe-method-to-get-value-of-nested-dictionary
def deep_get(dictionary, keys, default = None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split('.'), dictionary)


def extract_product_images(data) -> list:
    if deep_get(data, 'data.styleImages') is None:
        return []

    images = []
    for key in deep_get(data, 'data.styleImages'):
        img = deep_get(data, 'data.styleImages.{}.imageURL'.format(str(key)))

        if img: 
            images.append(ProductImage(url = img))
        continue
    return images
        

def extract_product_colors(data) -> list:
    colors_list = []

    if deep_get(data, "data.baseColour") is not None:
        primary_color = deep_get(data, "data.baseColour")
        secondary_color = deep_get(data, "data.colour1")
        url = deep_get(data, "data.styleImages.default.imageURL")

        colors_list.append(
            ProductColor(
                primary_color = primary_color,
                secondary_color = None if (secondary_color == "NA") or (secondary_color == "") else secondary_color,
                url = url
            )
        )

    if deep_get(data, "data.colours.colors") is not None:
        for key in deep_get(data, "data.colours.colors").keys():
            primary_color = deep_get(data, f"data.colours.colors.{str(key)}.global_attr_base_colour")
            secondary_color = deep_get(data, f"data.colours.colors.{str(key)}.global_attr_colour1")
            color_url = deep_get(data, f"data.colours.colors.{str(key)}.search_image")

            colors_list.append( 
                ProductColor(
                    primary_color = primary_color,
                    secondary_color = None if (secondary_color == "NA") or (secondary_color == "") else secondary_color,
                    url = color_url
                ) 
            )
    return colors_list


def extract_product_sizes(data) -> list:
    if deep_get(data, 'data.styleOptions') is None:
        return []

    sizes = []
    for item in deep_get(data, 'data.styleOptions'):
        size = deep_get(item, 'value')

        if size:
            sizes.append(ProductSize(value=size))
        continue
    return sizes


def data_creator():
    for file in os.listdir(os.path.join(get_base_dir(), "dataset")):
        name, ext = os.path.splitext(file)

        if ext != ".json" or int(name) not in range(10000, 15000):
            continue
        data = load_json_file(os.path.join(get_base_dir(), "dataset", file))

        print(deep_get(data, "data.id"))
            
        db.session.add(
            Product(
                id = deep_get(data, "data.id"),
                price = deep_get(data, "data.price"),
                name = deep_get(data, "data.productDisplayName"),
                brand_name = deep_get(data, "data.brandName"),
                gender = deep_get(data, "data.gender"),
                season = deep_get(data, "data.season"),
                year = deep_get(data, "data.year"),
                description = deep_get(data, "data.productDescriptors.description.value"),
                category = deep_get(data, "data.subCategory.typeName"),
                sub_category = deep_get(data, "data.articleType.typeName"),
                colors = extract_product_colors(data),
                images = extract_product_images(data),
                sizes = extract_product_sizes(data),
            )
        )
        db.session.commit()