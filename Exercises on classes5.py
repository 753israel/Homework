# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height
#
# r1 = Rectangle(20,20)
# print(r1.get_area())
#
#
# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         return False
#
# class ShoppingCart():
#     def __init__(self,products):
#         self.products = []
#
#     def add_product(self,name,price):
#         self.products.append((name,price))
#
#     def remove(self, name):
#         for product in self.products:
#             if product[0] == name:  # product[0] = שם המוצר
#                 self.products.remove(product)
#                 return
#         raise ValueError("Product not found")
#
# class Student:
#     def __init__(self,name,grades=None):
#         self.name = name
#         self.grades = grades if grades is not None else []
#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def get_average(self):
#         return sum(self.grades)/len(self.grades)
#     def has_passed(self):
#         if self.get_average() >= 60:
#             return True
#         return False
#
# class Playlist:
#     def __init__(self, songs=None):
#         self.songs = songs if songs is not None else []
#
#     def add_song(self, name, length):
#         self.songs.append((name, length))
#
#     def remove_song(self, name):
#         for song in self.songs:
#             if song[0] == name:
#                 self.songs.remove(song)
#                 return
#         raise ValueError("dont have a song name")
#
#     def total_length(self):
#         s = 0
#         for song in self.songs:
#             s += song[1]   # אורך השיר
#         return s
#
#     def find_song(self, name):
#         for song in self.songs:
#             if song[0] == name:
#                 return song
#         return None
#
from itertools import count

#
# class WordCounter:
#     def __init__(self, text):
#         self.text = text
#
#     def count_words(self):
#         words = self.text.split(" ")
#         return len(words)
#
#
# wc = WordCounter("hello world this is israel")
# print(wc.count_words())
