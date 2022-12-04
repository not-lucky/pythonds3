'''
REMEMBER THIS WHOLE SCRIPT WORKS ON THE PREMISE THAT ALL THE DOWNLOADS WILL BE SUCCESSFUL
UPDATE: MADE IT SLIGHTLY BETTER
TODO COMMENT THE CODE
'''

import requests
import json
import subprocess
from os import makedirs
from concurrent.futures import ThreadPoolExecutor

MANGADEX_API_BASE_URL = 'https://api.mangadex.org'

manga_list = requests.get(
    f'{MANGADEX_API_BASE_URL}/list/476a2c66-9f04-42d3-9b79-252cf3ca8416').json(
    )

# get manga_id for the mdlist 'to download' made and updated by me
manga_ids_list = [
    dic['id'] for dic in manga_list['data']['relationships']
    if dic['type'] == 'manga'
]


def read_file():
    with open('manga_and_last_chap.json', encoding='utf-8') as fl:
        json_file = json.load(fl)
    return json_file


def get_manga_list(manga_id):

    def manga_chapter_list(manga_id, downloaded_upto):
        some_shit = subprocess.check_output(
            f'gallery-dl -j --chapter-filter "lang == \'en\' and {downloaded_upto} < chapter" https://mangadex.org/title/{manga_id}',
            shell=True)
        json_data = json.loads(some_shit.decode('utf-8'))
        if json_data != []:
            chaps_dic = [(individual_chap_list[2]['chapter'],
                          individual_chap_list[2]['chapter_id'])
                         for individual_chap_list in json_data]

            return chaps_dic
        return None

    for manga_dic in manga_and_last_chap['ongoing']:
        if manga_dic == manga_id:
            return manga_chapter_list(
                manga_id,
                manga_and_last_chap['ongoing'][manga_dic]['last_chap_num'])
    return manga_chapter_list(manga_id, 0)


# def chapter_number_of_last_chapter():
#     a = subprocess.check_output('tail -n1 parallel_execute_commands.txt',
#                                 shell=True)
#     x = a.decode('utf-8').split()
#     last_chapter_id = x[-3].split('/')[-1]
#     chapter_number = requests.get(
#         f'{MANGADEX_API_BASE_URL}/chapter/{last_chapter_id}').json(
#         )['data']['attributes']['chapter']
#     return chapter_number


def get_chapter_image_info(chap_id):
    some_shit = subprocess.check_output(
        f'gallery-dl -j https://mangadex.org/chapter/{chap_id}', shell=True)
    chap_info = json.loads(some_shit.decode('utf-8'))
    return chap_info


def download_images_multithread(list_of_image_info_list):
    temp_var = list_of_image_info_list[0]
    print(
        f'Downloading {temp_var["manga_name"]}: Chapter {temp_var["chapter_number"]}-{temp_var["chapter_number"] + 4}'
    )

    def download_image(image_info_dic):
        try:
            directory = fr'manga/{image_info_dic["manga_name"]}/c{image_info_dic["chapter_number"]:0>3}'
            if image_info_dic['title'] != '':
                directory += f'_{image_info_dic["title"]}'
            makedirs(directory)
        except OSError:
            pass

        response = requests.get(image_info_dic['image_link'])
        with open(
                f"{directory}/{image_info_dic['manga_name']}_c{image_info_dic['chapter_number']:0>3}_{image_info_dic['page_number']:0>3}.{image_info_dic['extension']}",
                'wb') as handle:
            handle.write(response.content)

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(download_image, list_of_image_info_list)


def write_to_file(file, manga_and_last_chap, ongoing, manga_name, manga_id,
                  last_chapter_num):
    if ongoing == 'ongoing':
        manga_and_last_chap['ongoing'][manga_id] = {
            'manga_name': manga_name,
            'last_chap_num': last_chapter_num
        }
    else:
        manga_and_last_chap['completed'][manga_id] = {
            'manga_name': manga_name,
            'last_chap_num': last_chapter_num
        }
        if manga_id in manga_and_last_chap['ongoing']:
            del manga_and_last_chap['ongoing'][manga_id]

    with open(file, 'w', encoding='utf-8') as fl:
        json.dump(manga_and_last_chap, fl, indent=4)


# check if manga in mdlist thats not in completed list is completed or not
# if it is then put the manga in compeleted list and remove from ongoing if it is in there
# TODO remember to write the data to file
# SOME WORK TO DO HERE
for manga_id in manga_ids_list:
    manga_and_last_chap = read_file()
    if manga_id not in manga_and_last_chap['completed']:
        get_info_manga_id = requests.get(
            f'{MANGADEX_API_BASE_URL}/manga/{manga_id}').json()
        chapter_list = get_manga_list(manga_id)
        if chapter_list:
            for i in range(0, len(chapter_list), 4):
                list_of_image_info_list = []
                last_chapter = 0
                for k, v in chapter_list[i:i + 4]:
                    if k not in [
                            manga_and_last_chap['ongoing'][manga_dic]['last_chap_num']
                            for manga_dic in manga_and_last_chap['ongoing']
                            if manga_dic == manga_id
                    ]:
                        json_chapter_data = json.loads(
                            subprocess.check_output(
                                f'gallery-dl -j https://mangadex.org/chapter/{v}',
                                shell=True).decode('utf-8'))

                        for chapter_data in json_chapter_data:
                            if chapter_data[0] == 3:
                                list_of_image_info_list.append({
                                    'image_link':
                                    chapter_data[1],
                                    'manga_name':
                                    chapter_data[2]['manga'],
                                    'chapter_number':
                                    chapter_data[2]['chapter'],
                                    'title':
                                    chapter_data[2]['title'],
                                    'page_number':
                                    chapter_data[2]['page'],
                                    'extension':
                                    chapter_data[2]['extension']
                                })
                    last_chapter = k
                download_images_multithread(list_of_image_info_list)
                write_to_file(
                    file='manga_and_last_chap.json',
                    manga_and_last_chap=manga_and_last_chap,
                    ongoing=get_info_manga_id['data']['attributes']['status'],
                    manga_name=get_info_manga_id['data']['attributes']['title']
                    ['en'],
                    manga_id=get_info_manga_id['data']['id'],
                    last_chapter_num=last_chapter)
