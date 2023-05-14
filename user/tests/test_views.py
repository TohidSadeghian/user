# from rest_framework.test import APITestCase
# from user.models import Profile
# from django.urls import reverse
# from user.utils import otp_generate
# from common.utils import fake_generate
# from django.core.cache import cache


# class TestSetup(APITestCase):
   
#     def setUp(self) -> None:
#        self.code = otp_generate()
#        self.sub_login_url = reverse('sub_login')
#        self.confirm_url = reverse('confirm')
#        self.employee_login_url = reverse('employee_login')
#        self.employee_register_url = reverse('employee_register')
#        self.user_info_url = reverse('user_info')
#        self.mobile_number = '09{}'.format(fake_generate('1234567890'))
#        self.username = fake_generate('acdefghijklmnopqrstuvwxyz')
#        self.password = fake_generate('abcdefghijklmnopqrstuvwxyz123456789')
#        return super().setUp()
    
#     def tearDown(self) -> None:
#         return super().tearDown()

# class TestViews(TestSetup):

    
#     def test_user_cannot_register_with_no_data(self):
#         res = self.client.post(self.sub_login_url)
#         self.assertEqual(res.status_code,400)

#     def test_user_can_register_and_send_code_to_him(self):
#         user_data = {'username':self.username,'mobile_number':self.mobile_number}
#         res = self.client.post(self.sub_login_url,user_data,format='json')
#         self.assertEqual(res.status_code,200)

#     def test_user_cannot_confirm_his_mobile_number_with_no_data(self):
#         res = self.client.post(self.confirm_url)
#         self.assertEqual(res.status_code,400)

#     def test_user_confirm_his_mobile_number(self):
#         cache.set(f'code_{self.mobile_number}',self.code)
#         cache.set_many({f'mobile_{self.mobile_number}':self.mobile_number,f'username_{self.mobile_number}':self.username})
#         user_data = {'mobile_number':self.mobile_number,'code':self.code}
#         res = self.client.post(self.confirm_url,user_data,format='json')
#         self.assertEqual(res.status_code,200)
        
#     def test_user_can_login(self):
#         Profile.objects.create_user(username = self.username,mobile_number = self.mobile_number,is_verified=True)
#         cache.set(f'code_{self.mobile_number}',self.code)
#         user_data = {'mobile_number':self.mobile_number,'code':self.code}
#         res = self.client.post(self.confirm_url,user_data,format='json')
#         self.assertEqual(res.status_code,200)

#     def test_employee_cannot_login_with_no_data(self):
#         res = self.client.post(self.employee_login_url,format='json')
#         self.assertEqual(res.status_code,400)

#     def test_employee_can_login(self):
#         Profile.objects.create_user(username = self.username,password=self.password)
#         user_data = {'username':self.username,'password':self.password}
#         res = self.client.post(self.employee_login_url,user_data,format='json')
#         self.assertEqual(res.status_code,200)


#     def test_admin_create_employee(self):
#         Profile.objects.create_superuser(username='admin',password=self.password)
#         admin_data = {'username':'admin','password':self.password}
#         login_res = self.client.post(self.employee_login_url,admin_data,format='json')
#         access_token = login_res.json()['detail'].get('access')
#         user_data = {'username':'user','password':self.password,'role':'cashier'}
#         headers={'HTTP_AUTHORIZATION':f'Bearer {access_token}'}
#         register_res = self.client.post(self.employee_register_url,user_data,**headers)
#         self.assertEqual(register_res.status_code,201)
        
#         #check validation of password
#         user_data = {'username':'new_user','password':'1234','role':'cook'}
#         register_res = self.client.post(self.employee_register_url,user_data,**headers)
#         self.assertEqual(register_res.status_code,400)
    
#     def test_user_doesnot_have_any_permissiom_to_createe_employee(self):
#         Profile.objects.create_user(username='user',password=self.password)
#         user_data = {'username':'user','password':self.password}
#         login_res = self.client.post(self.employee_login_url,user_data,format='json')
#         access_token = login_res.json()['detail'].get('access')
#         user_data = {'username':self.username,'password':self.password,'role':'cook'}
#         headers={'HTTP_AUTHORIZATION':f'Bearer {access_token}'}
#         register_res = self.client.post(self.employee_register_url,user_data,**headers)
#         self.assertEqual(register_res.status_code,403)

#     def test_user_can_retrieve_and_update_his_information(self):
#         Profile.objects.create_user(username=self.username,email='user@yahoo.com',password=self.password)
#         user_data = {'username':self.username,'password':self.password}
#         login_res = self.client.post(self.employee_login_url,user_data,format='json')
#         access_token = login_res.json()['detail'].get('access')
#         headers={'HTTP_AUTHORIZATION':f'Bearer {access_token}'}
#         res = self.client.get(self.user_info_url,**headers)
#         response_set = {'username', 'first_name', 'last_name', 'email'} 
#         self.assertEqual(res.status_code,200)
#         self.assertTrue(response_set == res.json().keys())

#         #update information by user
#         new_user_data = {'username':'new_username','email':'new_user@yahoo.com'}
#         new_res = self.client.patch(self.user_info_url,new_user_data,**headers)
#         self.assertEqual(new_res.status_code,200)

#         #check informations of user is chenged
#         res = self.client.get(self.user_info_url,**headers)
#         self.assertNotEqual(self.username,res.json()['username'])
#         self.assertEqual('new_username',res.json()['username'])















    

    





    



    





    







  



        

    

