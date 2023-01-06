from django.contrib import admin

from MyBlogs.models import userData ,pollsData , FAQs ,polls

class userDataAdmin(admin.ModelAdmin):
    list_display=('name','email','discription')
    
admin.site.register(userData,userDataAdmin)


class pollDataAdmin(admin.ModelAdmin):
    list_display = ('selected_op',)
    
admin.site.register(pollsData,pollDataAdmin)


    


class FAQsAdmin(admin.ModelAdmin):
    list_display = ('title', 'Ans','title1','Ans','title2','Ans2')
admin.site.register(FAQs,FAQsAdmin)


class pollsAdmin(admin.ModelAdmin):
    list_display = ('title','op1','op2','op3','op4')

admin.site.register(polls,pollsAdmin)