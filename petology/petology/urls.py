from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
"""petology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')), # custom users app
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

]

"""
curl -X POST -d "username=your_username&password=your_password" http://localhost:8000/api-token-auth/

curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imd1c3RhZiIsImV4cCI6MTcwMDQ5NzQ5OSwiZW1haWwiOiJndXN0YWZAZ3VzdGFmLmNvbSJ9.80NTQHcMMM-8aFwRAELT7s-00EogYLQbKdDJ_aneBzE"}%' http://localhost:8000/api-token-verify/
curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imd1c3RhZiIsImV4cCI6MTcwMDQ5NzU4MiwiZW1haWwiOiJndXN0YWZAZ3VzdGFmLmNvbSJ9.0vNd0CC8LfgSDv-Mv2vTeiRhjuoDb75dzfRbxF6pq6Y"}' http://localhost:8000/api-token-verify/

curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imd1c3RhZiIsImV4cCI6MTcwMDQ5NzU4MiwiZW1haWwiOiJndXN0YWZAZ3VzdGFmLmNvbSJ9.0vNd0CC8LfgSDv-Mv2vTeiRhjuoDb75dzfRbxF6pq6Y"}' http://localhost:8000/api-token-refresh/
"""