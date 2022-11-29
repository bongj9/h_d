from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LoginForm, JoinForm, ProfileForm, EditForm
from django.contrib import auth
from .models import Profile

# 메인 페이지
def home_view(request):
    return render(request, 'home.html')

# 로그인 페이지
def login_view(request):
    # login_data = LoginForm()
    return render(request, 'login.html')

#책장 수납장 리스트 페이지
def nav_list_view(request):
    return render(request, 'nav_list.html')

#상세 페이지
def product_detail_view(request):
    return render(request, 'product_detail.html')

#검색 페이지
def search_view(request):
    return render(request, 'search.html')

#회원가입 페이지
# def signup_view(request):
#     return render(request, 'signup.html')
def signup_view(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# # 로그인 유효성 검사
# def login_validate(request):
#     login_data = LoginForm(request.POST)
#
#     if login_data.is_valid():
#         user = auth.authenticate(username=request.POST['id'], password=request.POST['password'])
#         if user is not None:
#             if user.is_active:
#                 auth.login(request, user)
#                 return redirect('/')
#
#         error_message= '사용자 ID 또는 비밀번호를 잘못입력하였습니다.'
#         return render(request, 'login_page.html', {'login_data':login_data,'login_errors':error_message})
#     error_message= '로그인 폼이 이상합니다.개발자에게 연락하시길 바랍니다.'
#     return render(request, 'login_page.html', {'login_data':login_data,'login_errors':error_message})
#
# # 로그아웃
# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# # 회원가입 페이지
# def join_page(request):
#     if request.method =='POST':
#         form_data = JoinForm(request.POST)
#         profile_data = ProfileForm(request.POST)
#         if form_data.is_valid() and profile_data.is_valid():
#             # get_user_model helper 함수를 통해 모델 클래스 참조
#             User = auth.get_user_model()
#
#             username = form_data.cleaned_data['id']
#             password = form_data.cleaned_data['password1']
#
#             User.objects.create_user(username=username, password=password)
#
#             email_address = form_data.cleaned_data['email_address']
#             phone_number = profile_data.cleaned_data['phone_number']
#
#             # email, phone_number 등록
#             user_info = get_object_or_404(User, username=username)
#             user_info.email = email_address
#             user_info.profile.phone_number = phone_number
#
#             user_info.save()
#
#             return redirect('/')
#         else :
#             return render(request, 'signup.html', {'join_data':form_data, 'profile_data':profile_data})
#
#
#     else :
#         form_data = JoinForm()
#         profile_data = ProfileForm()
#
#     return render(request, 'signup.html', {'join_data':form_data, 'profile_data':profile_data})

# # 개인정보 수정 페이지
# def edit_user_info(request):
#     # User 모델 클래스 가져오기
#     User = auth.get_user_model()
#
#     # 로그인된 user 정보 가져오기
#     user_info = get_object_or_404(User, username = request.user.username)
#
#     if request.method =='POST':
#         form_data = EditForm(request.POST,instance = user_info)
#         profile_data = ProfileForm(request.POST, instance = user_info.profile)
#
#         if form_data.is_valid() and profile_data.is_valid():
#             password = form_data.cleaned_data['password1']
#             print(password)
#             email_address = form_data.cleaned_data['email_address']
#             phone_number = profile_data.cleaned_data['phone_number']
#
#             user_info.set_password(password)
#             user_info.email = email_address
#             user_info.profile.phone_number = phone_number
#
#             user_info.save()
#
#             user = auth.authenticate(username=request.user.username, password=password)
#             auth.login(request, user)
#
#             return redirect('/')
#         else :
#             return render(request, 'edit_user.html', {'form_data':form_data, 'profile_data':profile_data})
#
#     form_data = EditForm(instance = user_info)
#     profile_data = ProfileForm(instance = user_info.profile)
#
#     return render(request, 'edit_user.html', {'form_data':form_data, 'profile_data':profile_data})

