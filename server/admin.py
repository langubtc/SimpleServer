from django.contrib import admin

# Register your models here.
from .models import Ip
from .models import ServerInfo


class IpAdmin(admin.ModelAdmin):
    list_display = ('net_ip', 'netmask', 'created_time')
    list_filter = ('net_ip',)
    search_fields = ('net_ip',)



class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'ip', 'cpu', 'mem', 'disk', 'os_version', 's_type', 'net', 's_status')
    list_filter = ('s_type', 's_status')
    search_fields = ('server_name', 'ip')
    fieldsets = (
        (None, {
            'fields': (
                'server_name',
                'ip',
                'cpu',
                'mem',
                'disk',
                'net',
                'os_version',
                ('s_type','s_status')

            )
        }),
    )


admin.site.register(Ip, IpAdmin)
admin.site.register(ServerInfo, ServerInfoAdmin)
