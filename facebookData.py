import facebook
import urllib3
import requests

token = 'EAAJJKGubBZAUBAGvY8SZBI7YsM2re8AFBVDDjHyvx3hlMUvz8T3ICmrJM9Tq0aaTrY6etxX8wZCT3Ca1jCJzQgPM8x0OBLkzoL3fp4ROift98upJZBP8jQDP6GJPxhqBjKToO0XO61j39VnWQMcLuBnKThfro9Xx0QeuMuKmDWAvMsasdEvRRN21BHTPqNCAgHo1tRV85JmB80Di8VXJvJh5nYcMxtglXXttrG0yywZDZD'
search = 'hello'

test = requests.get("https://graph.facebook.com/search?access_token=" + token + "&q=" + search + "&type=post")

print(test)





