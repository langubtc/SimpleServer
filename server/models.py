from django.db import models

# Create your models here.

class Ip(models.Model):
    net_ip = models.GenericIPAddressField(verbose_name="IP地址")
    netmask = models.GenericIPAddressField(u'子网掩码',blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False,verbose_name='创建时间')

    def __str__(self):
        return "<IP: {} >".format(self.net_ip)
    class Meta:
        verbose_name = "主机IP"
        verbose_name_plural = verbose_name


class ServerInfo(models.Model):
    SERVER_TYPE = [
        (1,'云服务器'),
        (2,'物理机'),
        (3,'虚拟机'),
        (4,'PC机')
    ]

    SERVER_STATUS = [
        (1,'在使用'),
        (2,'备用中'),
        (3,'损坏')
    ]

    server_name = models.CharField(max_length=50,verbose_name='主机名')
    ip = models.OneToOneField('Ip',verbose_name="主机IP",on_delete=models.CASCADE)
    disk = models.FloatField(verbose_name='磁盘容量')
    mem = models.FloatField(verbose_name='内存容量')
    cpu = models.IntegerField(verbose_name='CPU核数')
    net = models.IntegerField(verbose_name='网络带宽')
    os_version = models.CharField(verbose_name="系统类型",max_length=50)
    s_type = models.IntegerField(choices=SERVER_TYPE,default=1,verbose_name='主机类型')
    s_status = models.IntegerField(choices=SERVER_STATUS,default=2,verbose_name='设备状态')
    mark = models.CharField(max_length=100,verbose_name='备注')
    created_time = models.DateTimeField(auto_now_add=True, editable=False,verbose_name='创建时间')

    def __str__(self):
        return "<Server: {} >".format(self.server_name)


    @classmethod
    def get_all(cls):
        return cls.objects.all()



    class Meta:
        verbose_name = "主机信息"
        verbose_name_plural = verbose_name




