from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login_admin',views.login_admin,name='login_admin'),
    path('registration',views.registration,name='registration'),
    path('menu',views.menu,name='menu'),
    #path('index1',views.index1,name='index1'),
    path('franchies',views.franchies,name='franchies'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('forget_password',views.forget_password,name='forget_password'),
    path('login_user',views.login_user,name='login_user'),
    path('menu_user',views.menu_user,name='menu_user'),
    path('orders_user',views.orders_user,name='orders_user'),
    path('updateprofile_user',views.updateprofile_user,name='updateprofile_user'),
    path('messages_user',views.messages_user,name='messages_user'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('menu_admin',views.menu_admin,name='menu_admin'),
    path('additem_admin',views.additem_admin,name='additem_admin'),
    path('edit_menu/<str:item_id>',views.edit_menu,name='edit_menu'),
    path('delete_menu/<str:item_id>',views.delete_menu,name='delete_menu'),
    path('message_admin',views.message_admin,name='message_admin'),
    path('change_password',views.change_password,name='change_password'),
    path('total_admin',views.total_admin,name='total_admin'),
    path('ee/<str:item_id>',views.ee,name='ee'),
    path('checkout',views.checkout,name='checkout'),
    path('checkoutmain',views.checkout_main,name='checkout_main'),
    path('logout',views.logout,name='logout'),
    path('see_cart',views.see_cart,name='see_cart'),
    path('addtocart/<str:item_id>',views.addtocart,name='addtocart'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('changetopending/<str:id>',views.changetopending,name='changetopending'),
    path('changetodelivered/<str:id>',views.changetodelivered,name='changetodelivered'),
    path('removeitem/<str:item_id>',views.removeitem,name='removeitem')

]

