# from rest_framework.test import APITestCase
# from user.models import UserModels
# from user.utils import token_generate
# from django.core.cache import cache
# from rest_framework.exceptions import ValidationError,NotAcceptable


# class TestSetup(APITestCase):
   
#     def setUp(self) -> None:
#        self.initial_data = {}.fromkeys({'user_id', 'password', 'username', 'token'}, token_generate())
#        return super().setUp()
    
#     def tearDown(self) -> None:
#         return super().tearDown()

# class TestProfileModel(TestSetup):

#     def create_usermodel(self):
#         return UserModels.objects.create_user(
#             username = self.initial_data['username'],
#             password = self.initial_data['password'],
#             user_id  = self.initial_data['user_id']
#         )
    
#     def test_usermodel_creation(self):
#         user = self.create_usermodel()
#         self.assertTrue(isinstance(user, UserModels))
#         self.assertEqual(user.__str__(), self.initial_data['username'])

#     def test_usermodel_tokens(self):
#         user = self.create_usermodel()
#         self.assertTrue({'refresh','access'} == user.tokens().keys())
    
#     def test_usermodel_token_generator(self):
#         user = self.create_usermodel()
#         token = user.token_generator()
#         user_id = self.initial_data['user_id']
#         cached_token = cache.get(f"{token}_{user_id}")
#         self.assertTrue((token, user_id) == cached_token)

    # def test_usermodel_decrypt_token(self):
    #     user_id = self.initial_data['user_id']
    #     token = self.initial_data['token']
    #     cache.set(f"{token}_{user_id}", (token, user_id))
    #     res =  UserModels.decrypt_token(token)
    #     print(res)
    #     # self.assertTrue((token, user_id) == cached_token)
    

        






             




            


        



        


    


