import json
import requests
import time

class YogiyoCrawlerReview:

    def __init__(self):
        pass

    def get_json(self, url):

        payload = {}
        '''
        headers = {
          'x-apikey': 'iphoneap',
          'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2'
        }
        '''

        try:
            response = requests.request("GET", url,data = payload)
        except:
            print("ZZzzzz...")
            time.sleep(6)  # 너무 많은 request로 에러가 발생할 수 있으므로 잠시 쉰다
            return []  # 에러 발생 후 리스트를 리턴하여 해당번호는 패스하게 만듬

        json_data = response.json()
        # print(json_data)
        return json_data

    def get_json_review(self, start, end):
        json_list = []
        for index in range(start, end):
            index = str(index).zfill(6)
            url = f"https://www.yogiyo.co.kr/api/v1/reviews/{index}"
            ajson = self.get_json(url)
            if isinstance(ajson, dict):
                json_list.append(ajson)
            print(f'{index}번 크롤링 중')


        file_path = f"/Users/kuku/Desktop/anaconda/Yogiyo/data/json/review/yogiyo_review({start}~{end}).json"
        with open(file_path, 'w', encoding='UTF-8-sig') as file:
            json.dump(json_list, file, indent=4, ensure_ascii=False)
        print(f'yogiyo_review({start}~{end}).json 저장완료')







# file_path = "./sample.json"
# with open(file_path, "r", encoding="UTF-8-SIG") as json_file:
#     json_data = json.load(json_file)
#     # print(json_data)
#
# # print(type(json_data))  # <class 'dict'>
# restaurants = json_data["restaurants"]
# print(type(restaurants))  # <class 'list>


# import numpy as np
# a = np.array(list)
# print(np.median(a))
# print(max(list))
# print('리뷰내용:', restaurants[0]["comment"])
# print('메뉴이름:', restaurants[0]["menu_summary"])
# print('좋아요갯수:', restaurants[0]["like_count"])
# print('양평점:', restaurants[0]["rating_quantity"])
# print('맛평점:', restaurants[0]["rating_taste"])
# print('배달평점:', restaurants[0]["rating_delivery"])
# print('리뷰등록시간:', restaurants[0]["time"])
# print('리뷰등록이미지:', restaurants[0]["review_images"])    #full , thumb
# print('사장님댓글:', restaurants[0]["owner_reply"])     #comment(내용) , created_at(등록시간) , id



# print('최소 주문액:', restaurants[0]["min_order_amount"])
# print('영업 시간:', restaurants[0]["open_time_description"])
# print('리뷰 평점:', restaurants[0]["review_avg"])

# list = []
# # for i, item in enumerate(restaurants):
# for i in range(5):
#     list.append(restaurants[i]["id"])
#
# print(list)
#
# json_list = []


    # 메뉴정보 json 크롤링
    def menu_crawling(self):
        pass

# for item in list:
#     url = f"https://www.yogiyo.co.kr/api/v1/restaurants/{item}/menu"
#
#     payload = {}
#     headers = {
#       'x-apikey': 'iphoneap',
#       'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2'
#     }
#
#     response = requests.request("GET", url, headers=headers, data = payload)
#
#     json_data = response.json()
#     json_list.append(json_data)
# # print(json_data)
# # print(json_list)
# print(len(json_list))
#
# file_path = "./sample_menu.json"
# with open(file_path, 'w', encoding='UTF-8-sig') as file:
#     json.dump(json_list, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    yogiyo_crawler = YogiyoCrawlerReview()
    start = 10000
    end = 11000
    for i in range(500):
        yogiyo_crawler.get_json_review(start, end)
        start += 1000
        end += 1000
    # yogiyo_crawler.get_json_store(9000, 10000)